from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic.base import ContextMixin

from .models import *

class OnlineToolsView(View):
    def get(self, request):
        return render(request, "onlinetoolsone.html")

class OnlineToolsTwoView(View):
    def get(self, request):
        return render(request, "onlinetoolstwo.html")

class OnlineToolsThreeView(View):
    def get(self, request):
        return render(request, "onlinetoolsthree.html")

class OnlineToolsFourView(View):
    def get(self, request):
        return render(request, "onlinetoolsfour.html")

class OnlineToolsFiveView(View):
    def get(self, request):
        return render(request, "onlinetoolsfive.html")

class OnlineToolsSixView(View):
    def get(self, request):
        return render(request, "onlinetoolssix.html")

class OnlineToolsSevenView(View):
    def get(self, request):
        return render(request, "onlinetoolsseven.html")

class OnlineToolsEightView(View):
    def get(self, request):
        return render(request, "onlinetoolseight.html")

class OnlineToolsHomeView(View):
    def get(self, request):
        return render(request, "onlinetoolshome.html")

class OnlineToolsNineView(View):
    def get(self, request):
        return render(request, "onlinetoolsnine.html")

class OnlineToolsTenView(View):
    def get(self, request):
        return render(request, "onlinetoolsten.html")

class OnlineToolsTwelveView(View):
    def get(self, request):
        return render(request, "onlinetoolstwelve.html")

class NewView(View):
    def get(self, request):
        return render(request, "new.html")
