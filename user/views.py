import json

import stripe
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, TemplateView

from dynamic.models import Subdomain
from services.OrderDataService import OrderDataService
from services.StripeService import StripeService
from user.decorators import unauthenticated_user
from user.models import Portal, PortalGoal
from user.models import Profile

stripe.api_key = 'sk_test_51KMCX0LtISMk6veGzq2VeFxgp1aNpIz68d8Da3hkGsGtaBZS4aloZVsqAagNrPo45ya9mVgLdY4v1S7OBv8CJG2x006QLtNPUf'


class GDTLoginView(LoginView):
    template_name = 'login.html'
    print('from gdt login view')
    def form_valid(self, form):
        """Security check complete. Log the user in."""
        user = form.get_user()
        print(user,'from the gdtlogin view')
        auth_login(self.request, user)
        return HttpResponseRedirect(self.get_redirect_url() or '/dashboard')


class APIloginView(View):
    def get(self, request):
        data = request.GET
        if 'user' in data and 'pass' in data and 'redirect' in data:
            username = data['user']
            password = data['pass']
            redirect = data['redirect']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(redirect)

        return HttpResponseRedirect("/user/login")


@method_decorator(unauthenticated_user, name='dispatch')
class SignUpView(View):
    def get(self, request):
        obj = Subdomain.objects.filter(sub_name__exact=request.host.name).first()
        context = {}
        context["stripe_key"] = settings.STRIPE_PUBLISHABLE_KEY
        # print(context)
        return render(request, 'registration.html', context=context)

    @csrf_exempt
    def post(self, request):
        data = request.POST
        sub_domain = request.host.name
        # print(data)

        try:
            # print('try block')
            # obj = Subdomain.objects.filter(sub_name__exact=request.host.name).first()
            # print(obj.is_paid ,'the object')
            # if obj and obj.is_paid:
            #     print('paid')
            #     StripeService.charge_card(data['stripeToken'], round(obj.portal_price * 100),
            #                               description="registration")
            #     print('charged')
            profile = Profile.objects.create_user(data['email'], data['password'], data['first_name'],
                                                  data['last_name'], data['phone_number'], sub_domain)
            print(profile)
            auth_login(request, profile.user)
            print('logged in')
            return HttpResponseRedirect(reverse('homepage'))
        except Exception as e:
            if hasattr(e, 'message'):
                print('message')
                print(e.message)
            else:
                print(e)
                print('messages')
            return render(request, 'registration.html', {"error": "Registration Failed"})
        # return render(request, 'registration.html', {"error": "Registration Failed"})


class PasswordResetView(auth_views.PasswordResetView):
    from_email = 'Getdinerotoday@gmail.com'
    template_name = 'forgotpassword.html'

    @property
    def success_url(self):
        return reverse('user:password_reset_done')


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    @property
    def template_name(self):
        return 'resetPassword.html'

    @property
    def success_url(self):
        return reverse('user:password_change_done')


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    @property
    def template_name(self):
        return 'password-reset-email-sent.html'


class PasswordChangeDoneView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {"password_change_msg": "Successfully changed password", "form": form})


class MyProgressView(View):
    def get(self, request):
        request.resolver_match.app_name = 'business'
        context = {}
        stripe_user = StripeService.get_user_or_create_new(Profile.objects.get(user=request.user))
        context['stripe_user'] = stripe_user
        # context['source_cards'] = StripeService.get_payment_methods(stripe_user)
        # context['subscriptions'] = StripeService.get_user_subscriptions(stripe_user)
        context['source_cards'] = ""
        context['subscriptions'] = ""
        context['services'] = OrderDataService.get_user_steps_data(request.user)
        context['tradelines'] = OrderDataService.get_user_tradelines_data(request.user)
        return render(request, "my_progress.html", context=context)

    def post(self, request):
        data = request.POST
        profile = Profile.objects.get(user=request.user)
        if 'commit' in data and data['commit'] == "Save":
            user = request.user
            email_changed = data['email'] != user.email
            user.email = data['email']
            user.profile.phone_number = data['phone']
            user.save()
            user.profile.save()
            if email_changed:
                update_session_auth_hash(request, user)

        if 'delete_card' in data and data['delete_card'] == "Delete":
            if 'card' in data and data['card']:
                stripe.Customer.delete_source(
                    profile.stripe_id,
                    data['card'],
                )

        if 'create_card' in data and data['create_card'] == "Add":
            token = stripe.Token.create(
                card={
                    "number": data['cc_number'],
                    "exp_month": data['exp_month'],
                    "exp_year": data['exp_year'],
                    "cvc": data['cvc'],
                },
            )
            stripe.Customer.modify(profile.stripe_id, source=token)

        if 'cancel_subscription' in data and data['cancel_subscription'] == 'Unsubscribe':
            if 'subscription_id' in data and data['subscription_id']:
                stripe.Subscription.delete(data['subscription_id'])

        return HttpResponseRedirect(reverse('user:myprogress'))


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('user:login'))


class CreateSpecificPortal(TemplateView):
    template_name = "goals/create_my_portal.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(user= self.request.user)
        context['show_portal'] = profile.can_see_only_created_portals
        
        # not Required maybe in future
        # try:
        #     context['show_portal'] =Subdomain.objects.get(admins=profile,sub_name=self.request.host.name)
        #     print(context['show_portal'],'hello')
        # except Exception as e:
        #     context['show_portal']=False
        print(context['show_portal'])
        context['available_portals'] = Portal.objects.all()
        context['my_portals'] = PortalGoal.objects.filter(profile=self.request.user.profile)
        return context

    def post(self, request):
        data = request.POST
        name = data['name']
        portal_ids = json.loads(data['portals'])
        portal_goal = PortalGoal.objects.create(name=name, profile=request.user.profile)
        portal_goal.portals.set(portal_ids)

        return HttpResponseRedirect("/business/create-my-specific-portal/")


def delete_portal_goal(request, pk):
    try:
        obj = PortalGoal.objects.get(pk=pk)
        obj.delete()
    finally:
        return HttpResponseRedirect("/business/create-my-specific-portal/")


class PortalGoalsDetailView(LoginRequiredMixin, DetailView):
    model = PortalGoal
    template_name = "goals/portal_goals.html"
    context_object_name = 'portal_goal'

    def get_object(self, queryset=None):
        try:
            obj = PortalGoal.objects.get(slug=self.kwargs['slug'])
            return obj
        except PortalGoal.DoesNotExist:
            raise Http404

    def get_context_data(self, **kwargs):
        context = super(PortalGoalsDetailView, self).get_context_data(**kwargs)
        if 'slug' in self.kwargs:
            context['portal_number'] = self.kwargs['slug']
        return context


class TermsView(View):
    def get(self, request):
        return render(request, 'terms.html')
