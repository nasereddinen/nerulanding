from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic.base import ContextMixin

from .models import BusinessCreditCourse


class HomeView(View):
    def get(self, request):
        return render(request, "home.html")

class OneView(View):
    def get(self, request):
        return render(request, "one.html")


class TwoView(View):
    def get(self, request):
        return render(request, "2.html")

class ThreeView(View):
    def get(self, request):
        return render(request, "3.html")


class FourView(View):
    def get(self, request):
        return render(request, "4.html")

class FiveView(View):
    def get(self, request):
        return render(request, "5.html")


class SixView(View):
    def get(self, request):
        return render(request, "6.html")

class SevenView(View):
    def get(self, request):
        return render(request, "7.html")


class EightView(View):
    def get(self, request):
        return render(request, "8.html")

class NineView(View):
    def get(self, request):
        return render(request, "9.html")


class TenView(View):
    def get(self, request):
        return render(request, "10.html")

class ElevenView(View):
    def get(self, request):
        return render(request, "11.html")


class TwelveView(View):
    def get(self, request):
        return render(request, "twelve.html")


class ThirteenView(View):
    def get(self, request):
        return render(request, "13.html")


class FourteenView(View):
    def get(self, request):
        return render(request, "14.html")

class FifteenView(View):
    def get(self, request):
        return render(request, "15.html")


class SixteenView(View):
    def get(self, request):
        return render(request, "16.html")

class SeventeenView(View):
    def get(self, request):
        return render(request, "17.html")


class EighteenView(View):
    def get(self, request):
        return render(request, "18.html")

class NineteenView(View):
    def get(self, request):
        return render(request, "19.html")


class TwentyView(View):
    def get(self, request):
        return render(request, "20.html")

class TwentyoneView(View):
    def get(self, request):
        return render(request, "21.html")


class TwentytwoView(View):
    def get(self, request):
        return render(request, "22.html")

class TwentythreeView(View):
    def get(self, request):
        return render(request, "23.html")


class TwentyfourView(View):
    def get(self, request):
        return render(request, "24.html")

class TwentyfiveView(View):
    def get(self, request):
        return render(request, "25.html")


class TwentysixView(View):
    def get(self, request):
        return render(request, "26.html")

class TwentysevenView(View):
    def get(self, request):
        return render(request, "27.html")


class TwentyeightView(View):
    def get(self, request):
        return render(request, "28.html")

class TwentynineView(View):
    def get(self, request):
        return render(request, "29.html")


class ThirtyView(View):
    def get(self, request):
        return render(request, "30.html")

class ThirtyoneView(View):
            def get(self, request):
                return render(request, "31.html")

class ThirtytwoView(View):
            def get(self, request):
                return render(request, "32.html")
