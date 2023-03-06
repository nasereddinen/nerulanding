from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from financing_portal.models import ProductPurchasedModel, Product


class FinancingPortalHomeView(View):

    def get(self, request):
        profile = request.user.profile
        return render(request, 'FinancingPortalHomePage.html', {"profile": profile})


class FinancingPortalProductsPurchasedView(View):

    def get(self, request):
        products = ProductPurchasedModel.objects.filter(user=request.user)
        return render(request, 'FinancingPortalProductsPurchased.html', {"products": products})


class FinancingPortalPurchaseProductsView(View):

    def get(self, request):
        products = Product.objects.all()
        return render(request, 'FinancingPortalPurchaseProducts.html', {"products": products})

    def post(self, request):
        prod_id = request.POST.get('product_id')
        obj = Product.objects.filter(product_id=prod_id).first()

        if obj:
            ordering_products = [{
                'name': f"{obj.name}",
                'price': float(obj.price) + float(obj.charge),
                'quantity': 1,
                'type': 'financingProduct',
                'product_id': obj.product_id,
                'price_id': obj.price_id,
            }]
            request.session['ordering_products'] = ordering_products
        return redirect("business:stripe_checkout")


class FinancingPortalPaymentsView(View):

    def get(self, request):
        prods = ProductPurchasedModel.objects.filter(user=request.user)
        amount_left = 0
        payments_left = 0
        for i in prods:
            amount_left += i.amount_left
            payments_left += i.payments_left

        return render(request, 'FinancingPortalPayments.html', {
            "amount_left": amount_left,
            "payments_left": payments_left
        })


class FinancingPortalAccessSoftware(TemplateView):
    template_name = 'FinancingPortalProductsAccessSoftware.html'

    def get_context_data(self, **kwargs):
        products = ProductPurchasedModel.objects.filter(user=self.request.user)
        return {"products": products}
