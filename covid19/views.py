from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic.base import ContextMixin


class CoronaOneView(View):
    def get(self, request):
        return render(request, "coronaone.html")

class CoronaTwoView(View):
    def get(self, request):
        return render(request, "coronatwo.html")

class HomeOneView(View):
    def get(self, request):
        return render(request, "homeone.html")

class CoronaThreeView(View):
    def get(self, request):
        return render(request, "coronathree.html")


class CoronaFourView(View):
    def get(self, request):
        return render(request, "coronafour.html")

class CoronaFiveView(View):
    def get(self, request):
        return render(request, "coronafive.html")


class CoronaSixView(View):
    def get(self, request):
        return render(request, "coronasix.html")


class CoronaSevenView(View):
    def get(self, request):
        return render(request, "coronaseven.html")

class CoronaEightView(View):
    def get(self, request):
        return render(request, "coronaeight.html")

class CoronaNineView(View):
    def get(self, request):
        return render(request, "coronanine.html")
