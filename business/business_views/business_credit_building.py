from django.forms.models import model_to_dict
from django.shortcuts import render, redirect
from django.views import View

from business.conf import get_context_for_all, industry_choices
from business.forms import BusinessCreditStepsForm
from dynamic.models import Subdomain
from orders.models import UserSteps
from products.models import Tradelines, UserStepsProduct
from services.ModelServices import check_all_required_fields_filled
from services.StripeService import StripeService
from user.forms import UserDataForm
from user.models import Profile, UserData


class TradelinesView(View):

    def get(self, request):
        request.resolver_match.page_template = 'pages/base-business.html'
        subdomain = Subdomain.objects.filter(sub_name=request.host.name).first()
        tradelines = Tradelines.objects.filter(whitelabel_portal__sub_name=subdomain)
        data = UserData.objects.filter(user=Profile.objects.get(user=request.user)).first()
        if data:
            form = UserDataForm(None, instance=data)
        else:
            form = UserDataForm()

        error = request.session.get("formInvalid")

        return render(request, "financingProducts/tradelines.html",
                      context=get_context_for_all(request, {"tradelines": tradelines, "form": form, "error": error}))

    def post(self, request):

        print(request.POST)

        form = UserDataForm(request.POST)

        form.fields['duns'].required = True
        form.fields['billing_street_address_1'].required = True
        form.fields['billing_zip_code'].required = True
        form.fields['billing_city'].required = True
        form.fields['billing_state'].required = True
        form.fields['billing_country'].required = True
        form.fields['billing_phone'].required = True
        form.fields['website'].required = True
        form.fields['toll_free_number'].required = True
        form.fields['fax_number'].required = True

        if form.is_valid():
            data = UserData.objects.filter(user=Profile.objects.get(user=request.user)).first()
            if data:
                form = UserDataForm(request.POST, instance=data)
                new_data = form.save(commit=False)
                new_data.user = Profile.objects.get(user=request.user)
                new_data.save()
            else:
                new_data = form.save(commit=False)
                new_data.user = Profile.objects.get(user=request.user)
                new_data.save()
            if request.session.get('formInvalid'):
                request.session.pop('formInvalid')
        else:
            request.session['formInvalid'] = True
            return redirect("business:tradelines")

        if 'saveData' in request.POST:
            return redirect("business:tradelines")

        ordering_products = []
        product_id = request.POST['product_id']
        product = Tradelines.objects.get(product_id=product_id)
        ordering_products.append({
            'name': str(product),
            'price': float(product.price) + float(product.charge),
            'quantity': 1,
            'type': 'tradeline',
            'product_id': product.product_id,
            'price_id': product.price_id,
        })
        request.session['ordering_products'] = ordering_products
        user_data = UserData.objects.filter(user=Profile.objects.get(user=request.user)).first()
        if not user_data:
            return redirect("business:tradelines")
        if user_data and not check_all_required_fields_filled(user_data):
            return redirect("business:tradelines")

        return redirect("business:stripe_checkout")


class BusinessCreditStepsView(View):

    def get_user_steps(self, request):
        subdomain = Subdomain.objects.filter(sub_name=request.host.name).first()
        user_steps = UserStepsProduct.objects.filter(whitelabel_portal=subdomain)
        user_steps_obj = {
            "website": user_steps.filter(name="Website Monthly").first(),
            "toll_free_number": user_steps.filter(name="Toll Free Number Monthly").first(),
            "fax_number": user_steps.filter(name="Fax Number Monthly").first(),
            "domain": user_steps.filter(name="Domain Monthly").first(),
            "professional_email_address": user_steps.filter(name="Professional Email Address Monthly").first(),
            "website_year": user_steps.filter(name="Website Yearly").first(),
            "toll_free_number_year": user_steps.filter(name="Toll Free Number Yearly").first(),
            "fax_number_year": user_steps.filter(name="Fax Number Yearly").first(),
            "domain_year": user_steps.filter(name="Domain Yearly").first(),
            "professional_email_address_year": user_steps.filter(name="Professional Email Address Yearly").first(),
            "business_builder_program": user_steps.filter(name="Business builder program Monthly").first(),
            "business_builder_program_year": user_steps.filter(name="Business builder program Yearly").first(),
        }
        return user_steps_obj

    def get(self, request):
        template = "businessCreditBuilding/BusinessCreditSteps.html"
        if "standalone" in request.path:
            template = "businessCreditBuilding/BusinessCreditStepsStandalone.html"
        elif "onlyprograms" in request.path:
            template = "businessCreditBuilding/BusinessCreditStepsOnlyPrograms.html"
        user_steps = self.get_user_steps(request)
        user_data = UserData.objects.filter(user=Profile.objects.get(user=request.user)).first()
        form = BusinessCreditStepsForm()
        if user_data:
            da = model_to_dict(user_data)
            da['phone'] = user_data.personal_phone
            form = BusinessCreditStepsForm(da)

        return render(request, template, context=get_context_for_all(request, {"form": form,
                                                                               "user_steps": user_steps}))

    def post(self, request):
        avail_products = self.get_user_steps(request)
        ordering_products = []
        services = {}

        print(request.POST)

        for name, product in avail_products.items():
            if name in request.POST and request.POST[name] == 'on':
                ordering_products.append({
                    'name': str(product),
                    'price': float(product.price),
                    'quantity': int(request.POST.get(name + "_quantity", 1)),
                    'type': 'user_steps',
                    'product_id': product.product_id,
                    'price_id': product.price_id
                })
                service_in_model = name.replace("_year", "")
                services[service_in_model] = 2
                # if i in ['toll_free_number', 'fax_number', 'toll_free_number_year', 'fax_number_year']:
                #     services[i.replace("_year", "").replace("toll_free_number","toll_free") + "_quantity"] = request.POST.get(i + "_quantity")
                #     services[i.replace("_year", "") + "_prefix"] = request.POST.get(i + "_prefix")

        domain_name = ''
        if 'domain_name_year' in request.POST and request.POST['domain_name_year']:
            domain_name = request.POST['domain_name_year']
        if 'domain_name' in request.POST and request.POST['domain_name']:
            domain_name = request.POST['domain_name_year']
        industry_name = ''

        if 'industry_year' in request.POST and request.POST['industry_year']:
            industry_name = request.POST['industry_year']
        if 'industry' in request.POST and request.POST['industry']:
            industry_name = request.POST['industry']

        industry_choices_dict = {k: i for i, k in industry_choices}

        request.session['user_steps_data'] = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'domain_name': domain_name,
            'industry_name': industry_choices_dict.get(industry_name, 1),
            **services
        }

        request.session['ordering_products'] = ordering_products
        return redirect("business:stripe_checkout")


class BusinessCreditStepsGuidedView(View):

    def get_user_steps(self, request):
        subdomain = Subdomain.objects.filter(sub_name=request.host.name).first()
        user_steps = UserStepsProduct.objects.filter(whitelabel_portal=subdomain)
        user_steps_obj = {
            "website": user_steps.filter(name="Website Monthly").first(),
            "toll_free_number": user_steps.filter(name="Toll Free Number Monthly").first(),
            "fax_number": user_steps.filter(name="Fax Number Monthly").first(),
            "domain": user_steps.filter(name="Domain Monthly").first(),
            "professional_email_address": user_steps.filter(name="Professional Email Address Monthly").first(),
            "website_year": user_steps.filter(name="Website Yearly").first(),
            "toll_free_number_year": user_steps.filter(name="Toll Free Number Yearly").first(),
            "fax_number_year": user_steps.filter(name="Fax Number Yearly").first(),
            "domain_year": user_steps.filter(name="Domain Yearly").first(),
            "professional_email_address_year": user_steps.filter(name="Professional Email Address Yearly").first(),
            "business_builder_program": user_steps.filter(name="Business builder program Monthly").first(),
            "business_builder_program_year": user_steps.filter(name="Business builder program Yearly").first(),
        }
        return user_steps_obj

    def get(self, request):
        template = "businessCreditBuilding/steps/guidedCreation.html"

        user_steps = self.get_user_steps(request)
        user_data = UserData.objects.filter(user=Profile.objects.get(user=request.user)).first()
        form = BusinessCreditStepsForm()
        if user_data:
            da = model_to_dict(user_data)
            da['phone'] = user_data.personal_phone
            form = BusinessCreditStepsForm(da)

        return render(request, template, context=get_context_for_all(request, {"form": form,
                                                                               "user_steps": user_steps}))

    def post(self, request):
        avail_products = self.get_user_steps(request)

        offer_steps = ['LLC', 'EIN', 'business_account', 'merchant_account', 'duns', 'tradelines', 'marketing']
        offer_steps = {i: 2 for i in offer_steps if i in request.POST}

        ordering_products = []
        services = {}

        for name, product in avail_products.items():
            if name in request.POST and request.POST[name] == 'on':
                productToAppend = {
                    'name': str(product),
                    'quantity': int(request.POST.get(name + "_quantity", 1)),
                    'type': 'user_steps',
                }

                if hasattr(product, "price"):
                    productToAppend["price"] = float(product.price)
                else:
                    productToAppend["price"] = float(0)

                if hasattr(product, "product_id"):
                    productToAppend["product_id"] = product.product_id
                
                if hasattr(product, "price_id"):
                    productToAppend["price_id"] = product.price_id

                # ordering_products.append({
                #     'name': str(product),
                #     'price': float(product.price),
                #     'quantity': int(request.POST.get(name + "_quantity", 1)),
                #     'type': 'user_steps',
                #     'product_id': product.product_id,
                #     'price_id': product.price_id
                # })

                ordering_products.append(productToAppend)
                service_in_model = name.replace("_year", "")
                services[service_in_model] = 2
                # if i in ['toll_free_number', 'fax_number', 'toll_free_number_year', 'fax_number_year']:
                #     services[i.replace("_year", "").replace("toll_free_number","toll_free") + "_quantity"] = request.POST.get(i + "_quantity")
                #     services[i.replace("_year", "") + "_prefix"] = request.POST.get(i + "_prefix")

        domain_name = ''
        if 'domain_name_year' in request.POST and request.POST['domain_name_year']:
            domain_name = request.POST['domain_name_year']
        if 'domain_name' in request.POST and request.POST['domain_name']:
            domain_name = request.POST['domain_name_year']
        industry_name = ''

        if 'industry_year' in request.POST and request.POST['industry_year']:
            industry_name = request.POST['industry_year']
        if 'industry' in request.POST and request.POST['industry']:
            industry_name = request.POST['industry']

        industry_choices_dict = {k: i for i, k in industry_choices}

        request.session['user_steps_data'] = {
            'first_name': request.user.first_name,
            'last_name': request.user.first_name,
            'email': request.user.email,
            'phone': request.user.profile.phone_number,
            'domain_name': domain_name,
            'toll_free_number_prefix': request.POST.get('toll_free_number_prefix'),
            'fax_number_prefix': request.POST.get('fax_number_prefix'),
            'industry_name': industry_choices_dict.get(industry_name),
            # **offer_steps,
            **services,
        }

        new_steps = UserSteps(
            user=request.user,
            **offer_steps
        )
        new_steps.save()

        request.session['offer_steps'] = offer_steps
        request.session['ordering_products'] = ordering_products

        return redirect("business:stripe_checkout")


class WebsiteCreationView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'

        return render(request, 'businessCreditBuilding/websiteCreation.html', context=get_context_for_all(request))


class FaxNumberView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'
        return render(request, 'businessCreditBuilding/faxNumber.html', context=get_context_for_all(request))


class TollFreeNumberOptionsView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'

        profile = Profile.objects.filter(user=request.user)
        toll_free_number_paid = False
        if profile:
            toll_free_number_paid = profile[0].toll_free_number_paid
        if toll_free_number_paid:
            user_steps = UserSteps.objects.filter(user=request.user)
            services = []

            for i in user_steps:
                for k in ['toll_free_number']:
                    if getattr(i, k) == 2:
                        serv = {
                            'name': k.replace('_', " "),
                            'status': 'In progress',
                            'product': 'In progress',
                            'username': getattr(i, 'toll_free_username'),
                            'password': getattr(i, 'toll_free_password')
                        }
                        services.append(serv)
                    elif getattr(i, k) == 3:
                        serv = {
                            'name': k.replace('_', " "),
                            'status': 'Done',
                            'product': getattr(i, k + '_act'),
                            'username': getattr(i, 'toll_free_username'),
                            'password': getattr(i, 'toll_free_password')
                        }
                        services.append(serv)
            context = get_context_for_all(request)
            context['services'] = services

            return render(request, 'businessCreditBuilding/tollFreeNumberPaid.html', context=context)
        return render(request, 'businessCreditBuilding/tollFreeNumber.html', context=get_context_for_all(request))


class GuidedStepsView(View):
    def get(self, request):
        if request.resolver_match.app_name == 'goals':
            request.resolver_match.page_template = 'buildbusinesscredit/base-buildbusinesscredit.html'
        else:
            request.resolver_match.page_template = 'pages/base-business.html'

        steps = UserSteps.objects.filter(user=request.user)
        items = ['EIN', 'LLC', 'business_account', 'merchant_account', 'duns', 'tradelines', 'marketing']
        values = {i: 2 in steps.values_list(i, flat=True) for i in items}

        products = request.session.get('ordering_products')
        amount = 0
        if products:
            amount = sum([i['price'] * i['quantity'] for i in products])

        def_card = {
            'card_brand': '',
            'card_last4': ''
        }

        profile = Profile.objects.get(user=request.user)
        stripe_id = profile.stripe_id

        sources_available = []
        if stripe_id:
            stripe_user = StripeService.get_user_by_id(stripe_id)
            sources_available = stripe_user['sources']['data']
            if stripe_user['default_source']:
                add_new_payment_method = False
                cards_available = True
                card_id = stripe_user['default_source']
                for i in stripe_user['sources']['data']:
                    if i['id'] == card_id:
                        def_card['card_brand'] = i['brand']
                        def_card['card_last4'] = i['last4']
                        break
        if request.session.get('add_new_card'):
            add_new_payment_method = True
            request.session.pop('add_new_card')
        source_id = request.session.get('use_source_id')
        if source_id:
            for i in sources_available:
                if i['id'] == source_id:
                    def_card['card_brand'] = i['brand']
                    def_card['card_last4'] = i['last4']
                    break

        return render(request, 'businessCreditBuilding/steps/guidedStepsToDo.html',
                      context=get_context_for_all(request, {"values": values,
                                                            "products": products,
                                                            "amount": amount,
                                                            "def_card": def_card, }))
