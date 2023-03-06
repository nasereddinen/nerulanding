import json

from django.contrib.auth.models import User
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View

from affiliate.models import Webinar
from dynamic.models import Subdomain
from financing_portal.models import Product
from products.models import Tradelines, UserStepsProduct
from services.StripeService import StripeService
from services.WhiteLabelService import WhiteLabelService
from user.models import PortalGoal, Portal
from .forms import WhiteLabelForm
from .models import *


class HomeWhiteLabelView(View):
    def get(self, request):
        return render(request, "home-whitelabel.html")


class MarketingRoiView(View):
    def get(self, request):
        objects = MarketingRoi.objects.filter(user=request.user.profile)
        return render(request, "marketingroi.html", {"markentingroi": objects})


class PartnerCommissionView(View):
    def get(self, request):
        return render(request, "partner-commissions.html")


class BecomingAPartnerForm(ModelForm):
    class Meta:
        model = BecomingAPartner
        fields = ['business_name', 'business_number', 'logo']


def BecomingAPartner_update(request, pk, template_name='becomingapartner.html'):
    lead = get_object_or_404(BecomingAPartner, pk=pk)
    form = BecomingAPartnerForm(request.POST or None, instance=lead)
    if form.is_valid():
        form.save()
        return redirect('whitelabelpartnerportal:becomingapartner')

    return render(request, template_name, {'form': form})


class BecomingAPartnerView1(View):
    def get(self, request):
        partners = BecomingAPartner.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "becomingapartner1.html", {"partners": partners})

    def post(self, request):
        if 'delete' in request.POST:
            try:
                instance = BecomingAPartner.objects.get(id=request.POST['delete'])
                instance.delete()
                return redirect('whitelabelpartnerportal:becomingapartner1')
            except Exception as e:
                print(e)
                return redirect('whitelabelpartnerportal:becomingapartner1')

        else:
            try:
                data = {
                    'business_name': request.POST['business_name'],
                    'business_number': request.POST['business_number'],
                }
                if 'logo' in request.FILES:
                    data['logo'] = request.FILES['logo']

                new_lead = BecomingAPartner(user=Profile.objects.get(user=request.user), **data)
                new_lead.save()
            except Exception as e:
                print(e)
                data = {
                    'business_name': request.POST['business_name'],
                    'business_number': request.POST['business_number'],
                }
                new_lead = BecomingAPartner(user=Profile.objects.get(user=request.user), **data)
                new_lead.save()
            return redirect('whitelabelpartnerportal:becomingapartner1')


class BecomingAPartnerView(View):
    def get(self, request):
        return render(request, "becomingapartner.html")

    def post(self, request):

        if 'product' in request.POST:

            sub = Subdomain.objects.filter(sub_name=request.host.name).first()

            if request.POST['product'] == 'premium':
                product_name = "Premium Partnership Program"
                response = StripeService.create_product(product_name, float(sub.premium_partnership_program_price), recurring=2)
                ordering_products = [{
                    'name': product_name,
                    'price': float(sub.premium_partnership_program_price),
                    'quantity': 1,
                    'type': 'whitelabel',
                    'product_id': response['prod_id'],
                    'price_id': response['price_id'],
                }]
                request.session['ordering_products'] = ordering_products
            elif request.POST['product'] == 'basic':
                product_name = "Basic Partnership Program Package"
                response = StripeService.create_product(product_name, float(sub.basic_partnership_program_price), recurring=3)
                ordering_products = [{
                    'name': product_name,
                    'price': float(sub.basic_partnership_program_price),
                    'quantity': 1,
                    'type': 'whitelabel',
                    'product_id': response['prod_id'],
                    'price_id': response['price_id'],
                }]
                request.session['ordering_products'] = ordering_products

        return redirect("business:stripe_checkout")


class WhiteLabelTrainingView(View):
    def get(self, request):
        return render(request, "whitelabeltraining.html")


class MyResidualsView(View):
    def get(self, request):
        residuals = Residual.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "myresiduals.html", {"residuals": residuals})


class EnterNewLeadsView(View):
    def get(self, request):
        return render(request, "enternewleads.html")

    def post(self, request):
        data = {
            'first_name': request.POST['firstname'],
            'last_name': request.POST['lastname'],
            'business_name': request.POST['businessname'],
            'business_package': request.POST['businesspackage'],
        }
        new_lead = Lead(user=Profile.objects.get(user=request.user), **data)
        new_lead.save()
        return HttpResponseRedirect(reverse("whitelabelpartnerportal:leadoverview"))
        # return render(request, "enternewleads.html", {"submitted": True})


class LeadForm(ModelForm):
    class Meta:
        model = Lead
        fields = ['first_name', 'last_name', 'business_name', 'business_package']


def lead_update(request, pk, template_name='enternewleads.html'):
    lead = get_object_or_404(Lead, pk=pk)
    form = LeadForm(request.POST or None, instance=lead)
    if form.is_valid():
        form.save()
        return redirect('whitelabelpartnerportal:leadoverview')

    return render(request, template_name, {'form': form})


class LeadOverviewView(View):
    def get(self, request):
        leads = Lead.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "leadoverview.html", {"leads": leads})

    def post(self, request):
        if 'delete' in request.POST:
            try:
                instance = Lead.objects.get(id=request.POST['delete'])
                instance.delete()
            except Exception as e:
                pass
        return HttpResponseRedirect(reverse("whitelabelpartnerportal:leadoverview"))


class MySalesView(View):
    def get(self, request):
        sales = Sale.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "mysales.html", {"sales": sales})


class NetworkMarketingView(View):
    def get(self, request):
        return render(request, "networkmarketing.html")


class EnterAffiliatesView(View):
    def get(self, request):
        return render(request, "enteraffiliates.html")

    def post(self, request):
        data = {
            'full_name': request.POST['fullname'],
            'phone_number': request.POST['phonenumber'],

        }
        new_agent = AffiliateAgents(user=Profile.objects.get(user=request.user), **data)
        new_agent.save()
        return HttpResponseRedirect(reverse("whitelabelpartnerportal:salesaffiliates"))


class SalesAffiliatesView(View):
    def get(self, request):
        agents = AffiliateAgents.objects.filter(user=Profile.objects.get(user=request.user))

        return render(request, "salesaffiliates.html", {"agents": agents})

    def post(self, request):
        if 'delete' in request.POST:
            try:
                instance = AffiliateAgents.objects.get(id=request.POST['delete'])
                instance.delete()
            except Exception as e:
                pass
        return HttpResponseRedirect(reverse("whitelabelpartnerportal:salesaffiliates"))


class AffiliateAgentForm(ModelForm):
    class Meta:
        model = AffiliateAgents
        fields = ['full_name', 'phone_number']


def affiliate_agent_update(request, pk, template_name='enteraffiliates.html'):
    lead = get_object_or_404(AffiliateAgents, pk=pk)
    form = AffiliateAgentForm(request.POST or None, instance=lead)
    if form.is_valid():
        form.save()
        return redirect('whitelabelpartnerportal:salesaffiliates')
    return render(request, template_name, {'form': form})


class ResidualsFromAffiliatesView(View):
    def get(self, request):
        residuals = AffiliateResidual.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "residualsfromaffiliates.html", {"residuals": residuals})


class FreeSignupView(View):
    def get(self, request):
        sub_domain = request.host.name
        freeprograms = FreeProgram.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "freesignup.html", {"freeprograms": freeprograms})


class PaidSignupView(View):
    def get(self, request):
        user_data = WhiteLabelService.get_users_by_subdomains(request)
        return render(request, "paidsignup.html", {"user_data": user_data})


class OrdersView(View):
    def get(self, request):
        orders = Order.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "orders.html", {"orders": orders})


class InvoicesView(View):
    def get(self, request):
        invoices = Invoice.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "invoices.html", {"invoices": invoices})


class PaymentsView(View):
    def get(self, request):
        payments = Payment.objects.filter(user=Profile.objects.get(user=request.user))

        return render(request, "payments.html", {"payments": payments})


class CreditsView(View):
    def get(self, request):
        credits = Credit.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "credits.html", {"credits": credits})


class WholesalePackagesView(View):
    def get(self, request):
        return render(request, "WholeSaleSection/wholesalepackages.html")


class OfferingFinancingView(View):
    def get(self, request):
        return render(request, "offeringfinancing.html")


class WhiteLabelWebinarView(View):
    def get(self, request):
        webinars = Webinar.objects.filter(user=Profile.objects.get(user=request.user))

        return render(request, "whitelabelwebinar.html", {'webinars': webinars})


class BuyWhitelabelWebsiteView(View):
    def get(self, request):
        return render(request, "buywhitelabelwebsite.html")


class BuyWhitelabelBusinessPackageView(View):
    def get(self, request):
        return render(request, "buywhitelabelbusinesspackage.html")


class ViewPortalsView(View):
    def get(self, request):
        portals = WhitelabelPortal.objects.filter(user=Profile.objects.get(user=request.user))

        return render(request, "viewportals.html", {"portals": portals})


class ViewWhiteLabelWebsiteView(View):
    def get(self, request):
        sites = WhitelabelWebsite.objects.filter(user=Profile.objects.get(user=request.user))

        return render(request, "viewwhitelabelwebsite.html", {"sites": sites})


class ViewWhiteLabelBusinessPackageView(View):
    def get(self, request):
        packages = WhitelabelBusinessPackage.objects.filter(user=Profile.objects.get(user=request.user))

        return render(request, "viewwhitelabelbusinesspackage.html", {"packages": packages})


class AddBankInfoView(View):
    def get(self, request):
        banks = BankPaymentInformation.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "addbankinfo.html", {"banks": banks})

    def post(self, request):
        if 'delete' in request.POST:
            try:
                instance = BankPaymentInformation.objects.get(id=request.POST['delete'])
                instance.delete()
            except Exception as e:
                pass
        return HttpResponseRedirect(reverse("whitelabelpartnerportal:addbankinfo"))


class BankInfoForm(ModelForm):
    class Meta:
        model = BankPaymentInformation
        fields = ['routing_number', 'name_of_bank', 'account_number', 'name_on_bank_account', 'your_address']


def bank_info_update(request, pk, template_name='addbankinfo_form.html'):
    lead = get_object_or_404(BankPaymentInformation, pk=pk)
    form = BankInfoForm(request.POST or None, instance=lead)
    if form.is_valid():
        form.save()
        return redirect('whitelabelpartnerportal:addbankinfo')
    return render(request, template_name, {'form': form})


class AddBankInfoFormView(View):
    def get(self, request):
        return render(request, "addbankinfo_form.html")

    def post(self, request):
        data = {
            'routing_number': request.POST['routing_number'],
            'name_of_bank': request.POST['name_of_bank'],
            'account_number': request.POST['account_number'],
            'name_on_bank_account': request.POST['name_on_bank_account'],
            'your_address': request.POST['your_address'],

        }
        new_bank = BankPaymentInformation(user=Profile.objects.get(user=request.user), **data)
        new_bank.save()
        return HttpResponseRedirect(reverse("whitelabelpartnerportal:addbankinfo"))


class addZelleInfoView(View):
    def get(self, request):
        zelles = ZelleInformation.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "addzelleinfo.html",{'zelles':zelles})
    
    def post(self,request):
        if 'delete' in request.POST:
            try:
                instance = ZelleInformation.objects.get(id=request.POST['delete'])
                instance.delete()
            except Exception as e:
                pass
        return HttpResponseRedirect(reverse("whitelabelpartnerportal:addzelleinfo"))


class AddZelleInfoFormView(View):
    def get(self,request):
        print('the zelle infor form view ran ')
        return render(request, "addzelleinfo_form.html")
    
    def post(self,request):
        data = {'zelle_email':request.POST['zelle_email'],'zelle_phone':request.POST['zelle_phone']}
        print(data,'from the add zelle post view')
        new_bank = ZelleInformation(user=Profile.objects.get(user=request.user), **data)
        print(new_bank)
        new_bank.save()
        return HttpResponseRedirect(reverse("whitelabelpartnerportal:addzelleinfo"))

class AddPaypalInfoView(View):
    def get(self, request):
        paypals = PaypalInformation.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "addpaypalinfo.html", {"paypals": paypals})

    def post(self, request):
        if 'delete' in request.POST:
            try:
                instance = PaypalInformation.objects.get(id=request.POST['delete'])
                instance.delete()
            except Exception as e:
                pass
        return HttpResponseRedirect(reverse("whitelabelpartnerportal:addpaypalinfo"))


class AddPaypalInfoFormView(View):
    def get(self, request):
        return render(request, "addpaypalinfo_form.html")

    def post(self, request):
        data = {'paypal_email': request.POST['paypal_email']}
        new_bank = PaypalInformation(user=Profile.objects.get(user=request.user), **data)
        new_bank.save()
        return HttpResponseRedirect(reverse("whitelabelpartnerportal:addpaypalinfo"))


class ZelleInfoForm(ModelForm):
    class Meta:
        model = ZelleInformation
        fields = ['zelle_email','zelle_phone']
class PayPalInfoForm(ModelForm):
    class Meta:
        model = PaypalInformation
        fields = ['paypal_email']


def zelle_info_update(request,pk,template_name='addzelleinfo_form.html'):
    lead = get_object_or_404(ZelleInformation, pk=pk)
    form = ZelleInfoForm(request.POST or None, instance=lead)
    if form.is_valid():
        form.save()
        return redirect('whitelabelpartnerportal:addzelleinfo')
    return render(request, template_name, {'form': form})
def paypal_info_update(request, pk, template_name='addpaypalinfo_form.html'):
    lead = get_object_or_404(PaypalInformation, pk=pk)
    form = PayPalInfoForm(request.POST or None, instance=lead)
    if form.is_valid():
        form.save()
        return redirect('whitelabelpartnerportal:addpaypalinfo')
    return render(request, template_name, {'form': form})


class MerchantView(View):
    def get(self, request):
        return render(request, "merchant.html")


class FaxView(View):
    def get(self, request):
        return render(request, "fax.html")


class TollFreeView(View):
    def get(self, request):
        return render(request, "tollfree.html")


class ProfessionalEmailView(View):
    def get(self, request):
        return render(request, "professionalemail.html")


class ProductManagementView(View):
    def get(self, request):
        subdomain_products = WhiteLabelService.get_whitelabel_products(request)
        return render(request, "PortalManagement/productManagement.html", {"subdomain_products": subdomain_products})


class EditTradeline(View):
    def get(self, request):
        obj = Tradelines.objects.filter(product_id=request.GET.get('product')).first()
        return render(request, "PortalManagement/editTradeline.html", {"tradeline": obj})

    def post(self, request):
        print(request.POST)
        obj = Tradelines.objects.filter(product_id=request.POST.get('product')).first()
        if obj:
            obj.charge = float(request.POST.get('charge'))
            obj.save()
        return redirect("whitelabelpartnerportal:productmanagement")


class EditWholesale(View):
    def get(self, request):
        obj = WholeSale.objects.filter(product_id=request.GET.get('product')).first()
        return render(request, "PortalManagement/EditWholesalee.html", {"tradeline": obj})

    def post(self, request):
        print(request.POST)
        obj = WholeSale.objects.filter(product_id=request.POST.get('product')).first()
        if obj:
            obj.charge = float(request.POST.get('charge'))
            obj.price = float(request.POST.get('price'))
            obj.save()
        return redirect("whitelabelpartnerportal:productmanagement")


class EditSoftware(View):
    def get(self, request):
        obj = Product.objects.filter(product_id=request.GET.get('product')).first()
        return render(request, "PortalManagement/EditWholesalee.html", {"tradeline": obj})

    def post(self, request):
        print(request.POST)
        obj = Product.objects.filter(product_id=request.POST.get('product')).first()
        if obj:
            obj.charge = float(request.POST.get('charge'))
            obj.price = float(request.POST.get('price'))
            obj.save()
        return redirect("whitelabelpartnerportal:productmanagement")


class EditUserSteps(View):
    def get(self, request):
        obj = UserStepsProduct.objects.filter(product_id=request.GET.get('product')).first()
        return render(request, "PortalManagement/editUserSteps.html", {"userstep": obj})

    def post(self, request):
        print(request.POST)
        obj = UserStepsProduct.objects.filter(product_id=request.POST.get('product')).first()
        if obj:
            obj.price = float(request.POST.get('price'))
            obj.save()
        return redirect("whitelabelpartnerportal:productmanagement")


class ManageWhitelabel(View):
    def get(self, request):
        obj = WhiteLabelService.get_administrated_subdomains(request).first()
        form = WhiteLabelForm(instance=obj)
        return render(request, 'PortalManagement/ManageWhiteLabel.html', {'form': form, 'name': obj.sub_name})

    def post(self, request):
        obj = WhiteLabelService.get_administrated_subdomains(request).first()
        form = WhiteLabelForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()

        return redirect("whitelabelpartnerportal:manageportal")


class WholesaleView(View):
    def get(self, request):
        wholesales = WholeSale.objects.all()
        return render(request, 'WholeSaleSection/wholesales.html', {'wholesales': wholesales})

    def post(self, request):
        prod_id = request.POST.get('product_id')
        obj = WholeSale.objects.filter(product_id=prod_id).first()

        if obj:
            ordering_products = [{
                'name': f"{obj.name}",
                'price': float(obj.price) + float(obj.charge),
                'quantity': 1,
                'type': 'wholesale',
                'product_id': obj.product_id,
                'price_id': obj.price_id,
            }]
            request.session['ordering_products'] = ordering_products
        return redirect("business:stripe_checkout")


class ClientsOnWholesaleView(View):
    def get(self, request):
        clients = ClientsOnWholeSale.objects.filter(user=request.user)
        return render(request, 'WholeSaleSection/ClientsOnWholesale.html', {'clients': clients})


class PartnerResourceView(View):
    def get(self, request):
        resources = Resource.objects.all()
        categories = list(set([i.category for i in resources]))
        return render(request, 'WholeSaleSection/PartnerResources.html',
                      {'resources': resources, 'categories': categories})



class ClientCreatedByYouView(View):
    def get(self, request):
        clients = Profile.objects.filter(created_by=request.user.email)
        print(clients)
        return render(request, 'PortalManagement/AccountsCreatedByYou.html', {'clients': clients})
class CreateAccountView(View):
    """Create clients for your whitelabeladmin"""
    def get(self, request):
        
        return render(request, 'PortalManagement/CreateClientAccount.html', )

    def post(self, request):
        data = request.POST
        profile_user = Profile.objects.get(user=request.user)
        created_by=profile_user.user.email
        sub_domain = Subdomain.objects.filter(admins=profile_user).first()
        try:
            profile = Profile.objects.create_user(data['email'], data['password'], data['first_name'],
                                              data['last_name'], data['phone_number'],sub_domain, created_by)
        except Exception as e:
            print(e)
            return render(request, 'PortalManagement/CreateClientAccount.html',{'e':e})
  
        return render(request, 'PortalManagement/CreateClientAccount.html',{'profile':profile})

class ClientProgress(View):
    def get(self, request):
        profile_user = Profile.objects.get(user=request.user)
        print(profile_user)
        sub= Subdomain.objects.filter(admins=profile_user).first()
        print(sub)
        clients = Profile.objects.filter(whitelabel_portal=sub)
        print(clients)
        for i in clients:
            goals = []
            for k in i.portal_goals.all():
                for kk in k.portals.all().values('name'):
                    goals.append(kk)
            i.goals = goals

        return render(request, 'ClientProgress.html', {'clients': clients})

    def post(self, request):
        if 'create_portal' in request.POST:
            request.session['create_portal'] = request.POST.get('create_portal')
            return redirect('whitelabelpartnerportal:add_client_portal')

        elif 'see_only_created_portal' in request.POST:
            profile = Profile.objects.get(user=request.POST.get('see_only_created_portal'))
            print('see_only_created_portal')
            profile.can_see_only_created_portals = request.POST.get('can_see') == "on"
            print(request.POST.get('can_see') == "on")
            profile.save()
            print('profile saved')

        elif 'shut_of_client_account' in request.POST:
            user = User.objects.get(id=request.POST['shut_of_client_account'])
            if user.is_active:
                user.is_active=False
                user.save()
            else:
                user.is_active=True
                user.save()
            print( f"hi the user {user}is now active {user.is_active}")


        return redirect('whitelabelpartnerportal:clientProgress')


class AddClientPortals(View):
    def get(self, request):
        try:
            profile = Profile.objects.get(user__id=request.session.pop('create_portal'))
            portals = PortalGoal.objects.filter(profile=profile)
            available_portals = Portal.objects.all()

            context = {
                "profile": profile,
                "portals": portals,
                "available_portals": available_portals
            }

            return render(request, 'PortalManagement/ClientManagement.html', context)
        except:
            return redirect('whitelabelpartnerportal:clientProgress')

    def post(self, request):
        print(request.POST)
        if 'create_portal' in request.POST:
            request.session['create_portal'] = request.POST.get('create_portal')
            profile = Profile.objects.get(user__id=request.POST.get('create_portal'))
            data = request.POST
            name = data['name']
            portal_ids = json.loads(data['portals'])
            portal_goal = PortalGoal.objects.create(name=name, profile=profile)
            portal_goal.portals.set(portal_ids)

            return redirect('whitelabelpartnerportal:add_client_portal')
        return redirect('whitelabelpartnerportal:clientProgress')
