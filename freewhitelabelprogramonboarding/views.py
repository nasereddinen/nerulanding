from whitelabelpartnerportal.models import Resource, WhitelabelPortal
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic.base import ContextMixin

from .models import *

class OnboardingView(View):
    def get(self, request):
        return render(request, "onboarding.html")

class WhitelabelaccessView(View):
    def get(self, request):
        return render(request, "whitelabelaccess.html")



class PartnerResourceView(View):
    def get(self, request):
        resources = Resource.objects.all()
        categories = list(set([i.category for i in resources]))
        return render(request, 'partnerresources.html',
                      {'resources': resources, 'categories': categories})



class ViewPortalsView(View):
    def get(self, request):
        portals = WhitelabelPortal.objects.filter(user=Profile.objects.get(user=request.user))

        return render(request, "view-free-portals.html", {"portals": portals})
