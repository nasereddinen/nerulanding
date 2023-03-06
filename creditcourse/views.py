from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic.base import ContextMixin


class CarDealOneView(View):
    def get(self, request):
        return render(request, "carloanone.html")

class CreditRepairDoneView(View):
    def get(self, request):
        return render(request, "creditrepairdoneforyou.html")        

class MainFileView(View):
    def get(self, request):
        return render(request, "maincreditfile.html")

class CarDealTwoView(View):
    def get(self, request):
        return render(request, "carloantwo.html")

class MortgageOneView(View):
    def get(self, request):
        return render(request, "mortgageone.html")


class MortgageTwoView(View):
    def get(self, request):
        return render(request, "mortgagetwo.html")

class MortgageThreeView(View):
    def get(self, request):
        return render(request, "mortgagethree.html")


class MortgageFourView(View):
    def get(self, request):
        return render(request, "mortgagefour.html")


class RepairCreditOneView(View):
    def get(self, request):
        return render(request, "creditrepairone.html")

class RepairCreditTwoView(View):
    def get(self, request):
        return render(request, "creditrepairtwo.html")

class PersonalCreditOneView(View):
    def get(self, request):
        return render(request, "personalcreditone.html")

class PersonalCreditTwoView(View):
    def get(self, request):
        return render(request, "personalcredittwo.html")
class PersonalCreditThreeView(View):
    def get(self, request):
        return render(request, "personalcreditthree.html")

class PersonalCreditFourView(View):
    def get(self, request):
        return render(request, "personalcreditfour.html")
class PersonalCreditFiveView(View):
    def get(self, request):
        return render(request, "personalcreditfive.html")

class PersonalCreditSixView(View):
    def get(self, request):
        return render(request, "personalcreditsix.html")
class PersonalCreditSevenView(View):
    def get(self, request):
        return render(request, "personalcreditseven.html")

class PersonalCreditEightView(View):
    def get(self, request):
        return render(request, "personalcrediteight.html")
class PersonalCreditNineView(View):
    def get(self, request):
        return render(request, "personalcreditnine.html")

class PersonalCreditTenView(View):
    def get(self, request):
        return render(request, "personalcreditten.html")
class PersonalCreditElevenView(View):
    def get(self, request):
        return render(request, "personalcrediteleven.html")

class PersonalCreditTwelveView(View):
    def get(self, request):
        return render(request, "personalcredittwelve.html")
