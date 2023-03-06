from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic.base import ContextMixin

from .models import MarketingCourse


class RoiView(View):
    def get(self, request):
        return render(request, "roi.html")

class LtvView(View):
    def get(self, request):
        return render(request, "ltv.html")

class CpaView(View):
    def get(self, request):
        return render(request, "cpa.html")


class GooglerView(View):
    def get(self, request):
        return render(request, "googler.html")

class GoogleadsView(View):
    def get(self, request):
        return render(request, "googleads.html")


class SeoView(View):
    def get(self, request):
        return render(request, "seo.html")


class MainFileView(View):
    def get(self, request):
        return render(request, "mainfile.html")

class FacebookView(View):
    def get(self, request):
        return render(request, "facebook.html")

class YoutubeView(View):
    def get(self, request):
        return render(request, "youtube.html")

class FacebookrView(View):
    def get(self, request):
        return render(request, "facebookr.html")

class CouponsView(View):
    def get(self, request):
        return render(request, "coupons.html")
