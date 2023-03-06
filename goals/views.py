from django.shortcuts import render
from django.views import View


class RepairBusinessCreditView(View):
    def get(self, request):
        return render(request, "repairbusinesscredit/repairbusinesscredit.html")


class RepairBusinessCreditViewOne(View):
    def get(self, request):
        return render(request, "repairbusinesscredit/1.html")


class OfferingFinancingView(View):
    def get(self, request):
        return render(request, "offeringfinanicg/offeringfinancing.html")


class MerchantView(View):
    def get(self, request):
        return render(request, 'merchant/merchantaccount.html')


class MakeExtraMoneyView(View):
    def get(self, request):
        return render(request, 'makeextramoney/makeextramoney.html')


class ImmediateMoneyView(View):
    def get(self, request):
        return render(request, "immediatemoney/immediatemoney.html")


class ImmediateMoneyViewOne(View):
    def get(self, request):
        return render(request, "immediatemoney/1.html")


class ImmediateMoneyViewTwo(View):
    def get(self, request):
        return render(request, "immediatemoney/2.html")


class BuildBusinessCreditView(View):
    def get(self, request):
        return render(request, "buildbusinesscredit/buildbusinesscredit.html")


class BuildBusinessCreditViewOne(View):
    def get(self, request):
        return render(request, "buildbusinesscredit/1.html")


class BuildBusinessCreditViewTwo(View):
    def get(self, request):
        return render(request, "buildbusinesscredit/2.html")


class BuildBusinessCreditViewThree(View):
    def get(self, request):
        return render(request, "buildbusinesscredit/3.html")


class BuildBusinessCreditViewFour(View):
    def get(self, request):
        return render(request, "buildbusinesscredit/4.html")


class BuildBusinessCreditViewFive(View):
    def get(self, request):
        return render(request, "buildbusinesscredit/5.html")


class BuildBusinessCreditViewSix(View):
    def get(self, request):
        return render(request, "buildbusinesscredit/6.html")


class BuildBusinessCreditViewSeven(View):
    def get(self, request):
        return render(request, "buildbusinesscredit/7.html")


class BuildPersonalCreditView(View):
    def get(self, request):
        return render(request, "buildpersonalcredit/buildpersonalcredit.html")


class BuildPersonalCreditViewOne(View):
    def get(self, request):
        return render(request, "buildpersonalcredit/1.html")


class BuildPersonalCreditViewTwo(View):
    def get(self, request):
        return render(request, "buildpersonalcredit/2.html")


class BuildPersonalCreditViewThree(View):
    def get(self, request):
        return render(request, "buildpersonalcredit/3.html")


class MarketingBusinessView(View):
    def get(self, request):
        return render(request, "marketingbusiness/marketingbusiness.html")
