from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView

from dynamic.models import Subdomain
from orders.models import TradelineOrder, UserSteps
from products.models import Tradelines, UserStepsProduct
from services.StripeService import StripeService
from user.models import Profile, UserData

user_steps_obj = {
    "website": "Website Monthly",
    "toll_free_number": "Toll Free Number Monthly",
    "fax_number": "Fax Number Monthly",
    "domain": "Domain Monthly",
    "professional_email_address": "Professional Email Address Monthly",
    "website_year": "Website Yearly",
    "toll_free_number_year": "Toll Free Number Yearly",
    "fax_number_year": "Fax Number Yearly",
    "domain_year": "Domain Yearly",
    "professional_email_address_year": "Professional Email Address Yearly",
    "business_builder_program": "Business builder program Monthly",
    "business_builder_program_year": "Business builder program Yearly",
}
userstepsobj = {k: i for i, k in user_steps_obj.items()}


class TradelinesProductsAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        subdomain = Subdomain.objects.filter(sub_name=request.host.name).first()
        tradelines = Tradelines.objects.filter(whitelabel_portal__sub_name=subdomain)
        return Response(tradelines.values())


class UserStepsProductsAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        subdomain = Subdomain.objects.filter(sub_name=request.host.name).first()
        business_steps = UserStepsProduct.objects.filter(whitelabel_portal__sub_name=subdomain)
        return Response(business_steps.values())


class UserDataAPI(APIView):
    permission_classes = (IsAuthenticated,)

    class SomeModelSerializer(ModelSerializer):
        class Meta:
            model = UserData
            fields = "__all__"

    def get(self, request):
        data = UserData.objects.filter(user=Profile.objects.get(user=request.user)).first()
        return Response(self.SomeModelSerializer(data).data)

    def post(self, request):
        data = UserData.objects.filter(user=Profile.objects.get(user=request.user)).first()
        print(request.data)
        if 'id' in request.data:
            request.data.pop('id')
        request.data['user'] = Profile.objects.get(user=request.user)

        if data:
            for i, k in request.data.items():
                setattr(data, i, k)
            data.save()
        else:
            new_data = UserData(**request.data)
            new_data.save()

        return Response({'status': True})


class StripeOrderAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
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
            StripeService.add_source_to_user(stripe_id, data['stripeToken'])

        # Generate new subscriptions to products from session['ordering_products']
        products = data.get('products')
        if products and len(products) > 0:
            StripeService.make_purchases(products, stripe_id)

            addsteps = False
            steps_data = {}

            for i in products:
                if i['type'] == 'tradeline':
                    new_tradeline_order = TradelineOrder(user=request.user,
                                                         tradeline=Tradelines.objects.get(product_id=i['product_id']),
                                                         whitelabel_portal=Subdomain.objects.filter(
                                                             sub_name=data.get('subdomain')).first())
                    new_tradeline_order.save()
                elif i['type'] == 'user_steps':
                    addsteps = True
                    name = i.get("name")
                    if name in userstepsobj:
                        name = userstepsobj[name].replace("_year", "")
                        steps_data[name] = 2
            if addsteps:
                new_steps = UserSteps(
                    user=request.user,
                    **steps_data
                )
                new_steps.save()

            return Response({'response': "success"})
        else:
            return Response({'products': products})
        # # Add UserSteps if there is in session
        # user_steps_data = request.session.get('user_steps_data')
        # if user_steps_data:
        #     new_steps = UserSteps(
        #         user=request.user,
        #         **user_steps_data
        #     )
        #     new_steps.save()
        #     request.session.pop('user_steps_data')
        # for i in products:
        #     if i['type'] == 'tradeline':
        #         new_tradeline_order = TradelineOrder(user=request.user,
        #                                              tradeline=Tradelines.objects.get(product_id=i['product_id']),
        #                                              whitelabel_portal=Subdomain.objects.filter(
        #                                                  sub_name=request.host.name).first())
        #         new_tradeline_order.save()
        # amount = sum([i['price'] * i['quantity'] for i in products])
        # request.session.pop('ordering_products')
