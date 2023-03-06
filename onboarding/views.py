from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic.base import ContextMixin

from .models import *

class OnboardingView(View):
    def get(self, request):
        return render(request, "onboardinghome.html")

class BusinessTradelineView(View):
    def get(self, request):
        return render(request, "viewbusinesstradelines.html")

class DomainNameView(View):
    def get(self, request):
        return render(request, "viewdomainname.html")

class FaxNumberView(View):
    def get(self, request):
        return render(request, "viewfaxnumber.html")

class EmailView(View):
    def get(self, request):
        return render(request, "viewprofessionalemailaddress.html")

class SoftwarePurchaseView(View):
    def get(self, request):
        return render(request, "viewsoftwarepurchases.html")

class TollFreeView(View):
    def get(self, request):
        return render(request, "viewtollfree.html")

class WebsiteView(View):
    def get(self, request):
        return render(request, "viewwebsite.html")                                                        
