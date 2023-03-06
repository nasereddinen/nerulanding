from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import CreateView

from .forms import LeadForm
from .models import *


class HomeAffiliateView(View):
    def get(self, request):
        return render(request, "home-affiliate.html")

class CommissionView(View):
    def get(self, request):
        return render(request, "affiliate-commission.html")


class ShareLinksView(View):
    def get(self, request):
        return render(request, "affiliate-sharelinks.html")


class MyResidualsView(View):
    def get(self, request):
        residuals = Residual.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "affiliate-myresiduals.html", {"residuals": residuals})


class EnterNewLeadsView(View):
    def get(self, request):
        form = LeadForm()
        return render(request, "affiliate-enternewleads.html", {'form': form})

    def post(self, request):
        data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'business_name': request.POST['business_name'],
            'business_package': request.POST['business_package'],
        }
        new_lead = Lead(user=Profile.objects.get(user=request.user), **data)
        new_lead.save()
        return HttpResponseRedirect("/affiliate/leadoverview")
        # return render(request, "enternewleads.html", {"submitted": True})


def lead_update(request, pk, template_name='affiliate-enternewleads.html'):
    lead = get_object_or_404(Lead, pk=pk)
    form = LeadForm(request.POST or None, instance=lead)
    if form.is_valid():
        form.save()
        return redirect('/affiliate/leadoverview')

    return render(request, template_name, {'form': form})


class LeadOverviewView(View):
    def get(self, request):
        leads = Lead.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "affiliate-leadoverview.html", {"leads": leads})

    def post(self, request):
        if 'delete' in request.POST:
            try:
                instance = Lead.objects.get(id=request.POST['delete'])
                instance.delete()
            except Exception as e:
                pass
        return HttpResponseRedirect("/affiliate/leadoverview")


class MySalesView(View):
    def get(self, request):
        sales = Sale.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "affiliate-mysales.html", {"sales": sales})


class NetworkMarketingView(View):
    def get(self, request):
        return render(request, "affiliate-networkmarketing.html")


class AddBankInfoView(View):
    def get(self, request):
        banks = BankPaymentInformation.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "affiliate-addbankinfo.html", {"banks": banks})

    def post(self, request):
        if 'delete' in request.POST:
            try:
                instance = BankPaymentInformation.objects.get(id=request.POST['delete'])
                instance.delete()
            except Exception as e:
                pass
        return HttpResponseRedirect("/affiliate/addbankinfo")


class BankInfoForm(ModelForm):
    class Meta:
        model = BankPaymentInformation
        fields = ['routing_number', 'name_of_bank', 'account_number', 'name_on_bank_account', 'your_address']


def bank_info_update(request, pk, template_name='affiliate-addbankinfo_form.html'):
    lead = get_object_or_404(BankPaymentInformation, pk=pk)
    form = BankInfoForm(request.POST or None, instance=lead)
    if form.is_valid():
        form.save()
        return redirect('affiliate:affiliate-addbankinfo')
    return render(request, template_name, {'form': form})


class AddBankInfoFormView(View):
    def get(self, request):
        form = BankInfoForm()
        return render(request, "affiliate-addbankinfo_form.html", {'form': form})

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
        return HttpResponseRedirect("/affiliate/addbankinfo")


class AddPaypalInfoView(View):
    def get(self, request):
        paypals = PaypalInformation.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "affiliate-addpaypalinfo.html", {"paypals": paypals})

    def post(self, request):
        if 'delete' in request.POST:
            try:
                instance = PaypalInformation.objects.get(id=request.POST['delete'])
                instance.delete()
            except Exception as e:
                pass
        return HttpResponseRedirect("/affiliate/addpaypalinfo")


class AddPaypalInfoFormView(View):
    def get(self, request):
        form = PayPalInfoForm()
        return render(request, "affiliate-addpaypalinfo_form.html", {'form': form})

    def post(self, request):
        data = {
            'paypal_email': request.POST['paypal_email'],
        }
        new_bank = PaypalInformation(user=Profile.objects.get(user=request.user), **data)
        new_bank.save()
        return HttpResponseRedirect("/affiliate/addpaypalinfo")


class PayPalInfoForm(ModelForm):
    class Meta:
        model = PaypalInformation
        fields = ['paypal_email']


def paypal_info_update(request, pk, template_name='affiliate-addpaypalinfo_form.html'):
    lead = get_object_or_404(PaypalInformation, pk=pk)
    form = PayPalInfoForm(request.POST or None, instance=lead)
    if form.is_valid():
        form.save()
        return redirect('affiliate:affiliate-addpaypalinfo')
    return render(request, template_name, {'form': form})


class LeadCreateView(CreateView):
    model = Lead
    form_class = LeadForm
    template_name = "affiliate-enternewleads.html"
    success_url = "/affiliate/leadoverview"

    def form_valid(self, form):
        lead = form.save(commit=False)
        lead.user = self.request.user.profile
        lead.save()

        return HttpResponseRedirect("/affiliate/leadoverview")
