from django.shortcuts import render, redirect
from django.views import View

from business.conf import get_context_for_all
from business.models import Tier1, Tier2, Tier3, Tier4, CustomTier, NonReportingTradeline
from dynamic.models import Subdomain
from orders.models import TradelineOrder
from products.models import Tradelines
from services.OrderDataService import OrderDataService


class AllTradelinesView(View):
    def get(self, request):
        tier1 = Tier1.objects.all()
        tier2 = Tier2.objects.all()
        tier3 = Tier3.objects.all()
        tier4 = Tier4.objects.all()
        nonreporting = NonReportingTradeline.objects.all()
        subdomain = Subdomain.objects.filter(sub_name=request.host.name).first()
        our_tradelines = Tradelines.objects.filter(whitelabel_portal__sub_name=subdomain)
        current_tradelines = OrderDataService.get_user_tradelines_data(request.user)
        tradeline_count = len(current_tradelines)
        return render(request,
                      "BusinessCreditBuilderTracker/BusinessCreditBuilderTracker.html",
                      get_context_for_all(request, {
                          "tradeline_count": tradeline_count,
                          "current_tradelines": current_tradelines,
                          "tier1": tier1,
                          "tier2": tier2,
                          "tier3": tier3,
                          "tier4": tier4,
                          "nonreporting": nonreporting,
                          "our_tradelines": our_tradelines
                      }))

    def post(self, request):

        if 'our_tradeline' in request.POST and 'product_id' in request.POST:
            product_id = request.POST['product_id']
            product = Tradelines.objects.get(product_id=product_id)
            ordering_products = [{
                'name': str(product),
                'price': float(product.price) + float(product.charge),
                'quantity': 1,
                'type': 'tradeline',
                'product_id': product.product_id,
                'price_id': product.price_id,
            }]
            request.session['ordering_products'] = ordering_products
            return redirect("business:stripe_checkout")

        tiers = ['tier1', 'tier2', 'tier3', 'tier4', 'tier5']

        if 'tier' in request.POST and 'tradeline' in request.POST:
            tier = request.POST['tier']
            tradeline = request.POST['tradeline']
            print("wdfsdfsd", 'sds')

            if tier in tiers:
                obj = None
                t = 0
                if tier == 'tier1':
                    obj = Tier1.objects.filter(id=tradeline).first()
                    t = 1
                elif tier == 'tier2':
                    obj = Tier2.objects.filter(id=tradeline).first()
                    t = 2
                elif tier == 'tier3':
                    obj = Tier3.objects.filter(id=tradeline).first()
                    t = 3
                elif tier == 'tier4':
                    obj = Tier4.objects.filter(id=tradeline).first()
                    t = 4
                elif tier == 'tier5':
                    obj = NonReportingTradeline.objects.filter(id=tradeline).first()
                    t = 5
                if obj:
                    # print(obj)
                    ordering_products = [{
                        'name': f"{obj.company_name} {obj.product}",
                        'price': float(obj.price) + float(obj.charge),
                        'quantity': 1,
                        'type': 'tradeline',
                        'tier': t,
                        'product_id': obj.product_id,
                        'price_id': obj.price_id,
                    }]
                    request.session['ordering_products'] = ordering_products
                    # print("EHHEHEHE", ordering_products)
        return redirect("business:stripe_checkout")


class AddCustomTradelineView(View):
    def get(self, request):
        return render(request,
                      "BusinessCreditBuilderTracker/AddCustomTradelines.html",
                      get_context_for_all(request))

    def post(self, request):
        print(request.POST)

        tradeline = CustomTier(
            company_name=request.POST.get('company_name'),
            product=request.POST.get('product'),
            tradeline_amount=request.POST.get('tradeline_amount'),
            company_reports_to=request.POST.get('company_reports_to'),
            tradeline_credit_amount=request.POST.get('tradeline_credit_amount'),
        )
        tradeline.save()
        order = TradelineOrder(user=request.user, custom_tier=tradeline, which=-1)
        order.save()

        return redirect("business:business-credit-builder-tracker")
