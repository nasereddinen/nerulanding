from django.shortcuts import render
from django.views import View

from .models import *


class YourPlanView(View):
    def get(self, request):
        user = Profile.objects.get(user=request.user)

        plans = {
            "sezzle": Sezzle,
            "klarna": Klarna,
            "viabill": Viabill,
            "regularpayment": RegularPayment,
            "paypal": Paypal,
            "quadpay": Quadpay,
            "affirm": Affirm,
            "behalf": Behalf,
            "fundboxpay": FundBoxPay,
            "invoicefactoringpayment": InvoiceFactoringPayment,
            "stripe": Stripe,
        }

        data = {}
        total_owe = 0
        financed_so_far = 0
        financing_sources = []
        err = False
        for i, k in plans.items():
            filter = k.objects.filter(user=user)
            if len(filter) > 0:
                data[i] = filter[0]
                try:
                    total_owe += float(filter[0].how_much_owed)
                    financed_so_far += float(filter[0].financed_so_far)
                except Exception:
                    err = True
                financing_sources.append(i)
            else:
                data[i] = None
        if not err:
            data["total_owe"] = total_owe
            data["total_financed"] = financed_so_far
            data["financing_sources"] = ' , '.join(financing_sources)
        else:
            data["total_owe"] = "error"
            data["total_financed"] = "error"
            data["financing_sources"] = "error"

        return render(request, "yourplan.html", data)
