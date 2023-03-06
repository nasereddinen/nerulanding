from uuid import uuid4

from django.shortcuts import redirect, render
from django.views import View

from business.models import *
from dynamic.models import Subdomain
from financing_portal.models import ProductPurchasedModel, Product
from orders.models import TradelineOrder, UserSteps
from products.models import Tradelines
from services.StripeService import StripeService
from services.UsersService import UsersService
from whitelabelpartnerportal.models import WholeSaleOrder, WholeSale


def get_common_context(request, context=None):
    if not context:
        context = {}
    context["stripe_key"] = settings.STRIPE_PUBLISHABLE_KEY
    return context


class StripeCheckout(View):
    def get(self, request):
        UsersService.create_new_user_from_steps(self.request, request)

        profile = Profile.objects.get(user=request.user)
        # stripe_id = profile.stripe_id
        add_new_payment_method = True
        cards_available = False
        amount = 0
        def_card = {
            'card_brand': '',
            'card_last4': ''
        }
        sources_available = []
        # if stripe_id:
        #     stripe_user = StripeService.get_user_by_id(stripe_id)
        #     sources_available = stripe_user['sources']['data']
        #     if stripe_user['default_source']:
        #         add_new_payment_method = False
        #         cards_available = True
        #         card_id = stripe_user['default_source']
        #         for i in stripe_user['sources']['data']:
        #             if i['id'] == card_id:
        #                 def_card['card_brand'] = i['brand']
        #                 def_card['card_last4'] = i['last4']
        #                 break
        # if request.session.get('add_new_card'):
        #     add_new_payment_method = True
        #     request.session.pop('add_new_card')
        # source_id = request.session.get('use_source_id')
        # if source_id:
        #     for i in sources_available:
        #         if i['id'] == source_id:
        #             def_card['card_brand'] = i['brand']
        #             def_card['card_last4'] = i['last4']
        #             break

        products = request.session.get('ordering_products')
        if products:
            amount = sum([i['price'] * i['quantity'] for i in products])

        offer_steps = request.session.get('offer_steps')
        if offer_steps:
            request.session.pop('offer_steps')

        cart_uuid = uuid4()
        request.session['cart_uuid'] = str(cart_uuid)
        return render(request,
                      "checkout/stripeCheckout.html",
                      context=get_common_context(request, {
                                                            # "add_card": add_new_payment_method,
                                                        #    "def_card": def_card,
                                                           "amount": round(amount, 2),
                                                           "products": products,
                                                        #    "cards_available": cards_available,
                                                           "sources_available": sources_available,
                                                           "offer_steps": offer_steps
                                                           }))

    def post(self, request):
        data = request.POST
        if 'add_new_card' in data and data['add_new_card'] == 'Add New Card':
            request.session['add_new_card'] = True
        if 'back_to_checkout_cards' in data and data['back_to_checkout_cards'] == 'Back':
            request.session['back_to_checkout_cards'] = True
        if 'source_id' in data and data['source_id']:
            request.session['use_source_id'] = data['source_id']
        return redirect('business:stripe_checkout')


def subscription(request):
    if not request.session.get('cart_uuid'):
        return redirect("homepage")
    if request.method == 'POST':
        request.session.pop('cart_uuid')
        data = request.POST
        profile = Profile.objects.get(user=request.user)
        stripe_id = profile.stripe_id
        if not stripe_id:
            stripe_user = StripeService.create_user(
                first_name=request.user.first_name,
                last_name=request.user.last_name,
                email=request.user.email,
                source=data['stripeToken']
            )
            profile.stripe_id = stripe_user['id']
            profile.save()
            stripe_id = stripe_user['id']
        else:
            stripe_user = StripeService.get_user_by_id(stripe_id)
            if not stripe_user['default_source']:
                StripeService.add_source_to_user(stripe_id, data['stripeToken'])

        # Generate new subscriptions to products from session['ordering_products']
        products = request.session.get('ordering_products')
        source_id = request.session.get('use_source_id')
        StripeService.make_purchases(products, stripe_id, source_id)
        if source_id:
            request.session.pop('use_source_id')

        offer_steps = request.session.get('offer_steps')
        if offer_steps:
            request.session.pop('offer_steps')

        # Add UserSteps if there is in session
        user_steps_data = request.session.get('user_steps_data')
        if user_steps_data:
            new_steps = UserSteps(
                user=request.user,
                **user_steps_data
            )
            new_steps.save()
            request.session.pop('user_steps_data')

        for i in products:
            if i['type'] == 'tradeline':
                if 'tier' in i and i['tier'] == 1:
                    tradeline = {
                        'which': 1,
                        'tradeline_tier1': Tier1.objects.get(product_id=i['product_id'])
                    }
                elif 'tier' in i and i['tier'] == 2:
                    tradeline = {
                        'which': 2,
                        'tradeline_tier2': Tier2.objects.get(product_id=i['product_id'])
                    }
                elif 'tier' in i and i['tier'] == 3:
                    tradeline = {
                        'which': 3,
                        'tradeline_tier3': Tier3.objects.get(product_id=i['product_id'])
                    }
                elif 'tier' in i and i['tier'] == 4:
                    tradeline = {
                        'which': 4,
                        'tradeline_tier4': Tier4.objects.get(product_id=i['product_id'])
                    }
                elif 'tier' in i and i['tier'] == 5:
                    tradeline = {
                        'which': 5,
                        'non_reporting_tradeline': NonReportingTradeline.objects.get(product_id=i['product_id'])
                    }
                else:
                    tradeline = {
                        'which': 0,
                        'tradeline': Tradelines.objects.get(product_id=i['product_id'])
                    }

                new_tradeline_order = TradelineOrder(user=request.user,
                                                     whitelabel_portal=Subdomain.objects.filter(
                                                         sub_name=request.host.name).first(),
                                                     **tradeline)
                new_tradeline_order.save()
            elif i['type'] == 'wholesale':
                new_wholesale_order = WholeSaleOrder(user=request.user,
                                                     product=WholeSale.objects.get(product_id=i['product_id']))
                new_wholesale_order.save()
            elif i['type'] == 'financingProduct':
                product_order = ProductPurchasedModel(user=request.user,
                                                      product=Product.objects.get(product_id=i['product_id']))
                product_order.save()

        amount = sum([i['price'] * i['quantity'] for i in products])
        request.session.pop('ordering_products')
        return render(request, 'checkout/checkout.html', {'amount': amount})


def remove(request):
    if request.method == 'POST':
        data = request.POST
        if 'delete_item' in data and data['delete_item']:
            items = request.session.get('ordering_products')
            for i in items.copy():
                if i['name'] == data['delete_item']:
                    items.remove(i)
            request.session['ordering_products'] = items
        return redirect("business:stripe_checkout")


def charge(request):
    if request.method == 'POST':
        StripeService.charge_card(request.POST['stripeToken'], request.POST['amount'],
                                  'Get Dinero Today Service Charge')
        return render(request, 'checkout/checkout.html', {'amount': request.POST['amount']})
