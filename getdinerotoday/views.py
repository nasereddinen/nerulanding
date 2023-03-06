from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from dynamic.models import Subdomain
from products.models import UserStepsProduct
from business.models import NavigationLinks


def get_prices(sub_domain):
    obj = Subdomain.objects.filter(sub_name__exact=sub_domain).first()
    steps = UserStepsProduct.objects.filter(whitelabel_portal=obj)
    yearly = steps.filter(name="Business builder program Yearly").first()
    monthly = steps.filter(name="Business builder program Monthly").first()

    prices = {
        "yearly": 999,
        "monthly": 109.99
    }
    if yearly:
        prices['yearly'] = yearly.price
    if monthly:
        prices['monthly'] = monthly.price

    return prices


class HomePage(View):
    def get(self, request):
        request.resolver_match.app_name = 'business'
        if request.user.is_authenticated:
            links = NavigationLinks.objects.order_by('name')
            context = {'links': links}
            return render(request, 'homepage.html', context=context)
        else:
            return HttpResponseRedirect("/user/login")


class IndexView(View):
    def get(self, request):
        sub_domain = request.host.name
        obj = Subdomain.objects.filter(sub_name__exact=sub_domain).first()
        prices = get_prices(sub_domain)


        if obj:
            if request.user.is_authenticated:
                if obj.is_payment_done:
                    return render(request, 'landingpages/index.html', prices)
                return HttpResponseRedirect(reverse("homepage"))
            else:
                if obj.is_payment_done:
                    return render(request, 'landingpages/index.html', prices)
                return HttpResponseRedirect("/user/login")
        else:
            if request.user.is_authenticated:
                return HttpResponseRedirect(reverse("homepage"))
            return render(request, 'landingpages/index.html', prices)


class AboutUsView(View):
    def get(self, request):
        prices = get_prices(request.host.name)
        return render(request, 'landingpages/about-us.html', prices)


class PricingView(View):
    def get(self, request):
        prices = get_prices(request.host.name)
        return render(request, 'landingpages/pricing.html', prices)


class ServicesView(View):
    def get(self, request):
        prices = get_prices(request.host.name)
        return render(request, 'landingpages/services.html', prices)


class FinancingView(View):
    def get(self, request):
        return render(request, 'landingpages/financing.html')


class PartnerView(View):
    def get(self, request):
        return render(request, 'landingpages/partner.html')


class ContactView(View):
    def get(self, request):
        print(request.host.name)
        if request.host.name == 'www.kleui.com':
            context = {'True': True}
            return render(request, 'landingpages/contact.html',context)
        return render(request, 'landingpages/contact.html')

class CustomerSuccessAgentView(View):
    def get(self, request):
        return render(request, 'landingpages/customersuccessagent.html')


class WhiteLabelView(View):
    def get(self, request):
        return render(request, 'landingpages/whitelabel.html')


class Faqpartner(View):
    def get(self, request):
        return render(request, 'help/faqs.html')


class AffiliatelView(View):
    def get(self, request):
        return render(request, 'landingpages/affiliate.html')


class WebinarView(View):
    def get(self, request):
        return render(request, 'landingpages/webinar.html')


class WebinarOfferView(View):
    def get(self, request):
        return render(request, 'landingpages/webinaroffer.html')


class FAQView(View):
    def get(self, request):
        return render(request, 'help/faq.html')


class TestimonialsView(View):
    def get(self, request):
        return render(request, 'landingpages/testimonial.html')
