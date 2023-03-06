from rest_framework import serializers, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from dynamic.models import Subdomain
from services.WhiteLabelService import WhiteLabelService
from user.models import Profile
from whitelabelpartnerportal.models import Residual, Lead, Sale, Order, Invoice, Payment, Credit, \
    BankPaymentInformation, PaypalInformation


class ResidualsAPI(generics.ListAPIView):
    class ResidualsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Residual
            exclude = []

    serializer_class = ResidualsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        residuals = Residual.objects.filter(user=Profile.objects.filter(user=self.request.user).first())
        return residuals


class LeadsAPI(generics.ListAPIView):
    class LeadsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Lead
            exclude = []

    serializer_class = LeadsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        objects = Lead.objects.filter(user=Profile.objects.filter(user=self.request.user).first())
        return objects


class SalesAPI(generics.ListAPIView):
    class SalesSerializer(serializers.ModelSerializer):
        class Meta:
            model = Sale
            exclude = []

    serializer_class = SalesSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        objects = Sale.objects.filter(user=Profile.objects.filter(user=self.request.user).first())
        return objects


class SignedUsersAPI(APIView):
    class ProfileSerializer(serializers.Serializer):
        first_name = serializers.CharField(source='user.first_name')
        last_name = serializers.CharField(source='user.last_name')
        email = serializers.CharField(source='user.email')
        phone_number = serializers.CharField()
        updates_made = serializers.CharField()
        residual_amount = serializers.CharField()
        expected_payout = serializers.CharField()

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        objects = WhiteLabelService.get_users_by_subdomains(request)
        new_obj = []
        for i in objects:
            a = {
                'sub_name': i['sub_name'].sub_name,
                'users': self.ProfileSerializer(i['users'], many=True).data
            }
            new_obj.append(a)
        print(new_obj)

        return Response(new_obj)


class WhiteLabelLogoAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        objects = WhiteLabelService.get_administrated_subdomains(request)
        sub = objects.first()
        response = {
            'url': ''
        }

        if sub and sub.logo and sub.logo.url:
            response['url'] = sub.logo.url
        print(response)

        return Response(response)


class WhiteLabelUserLogoAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        profile = Profile.objects.filter(user=request.user).first()
        if profile.whitelabel_portal:
            subdomain = Subdomain.objects.filter(sub_name=profile.whitelabel_portal).first()
            if subdomain:
                responseobj = {
                    "status": True,
                    "url": subdomain.logo.url,
                    "bgColor": subdomain.bg_color,
                    "subdomain": subdomain.sub_name,
                    "title": subdomain.title,
                    "webinar": subdomain.webinar,
                    "extensionVideo": subdomain.extensionVideo,
                }
                return Response(responseobj)

        return Response({"status": False,
                         "webinar": 'https://www.youtube.com/watch?v=xNCfnbGT5hY',
                         "extensionVideo": 'https://www.youtube.com/embed/Z1HK9uSOMCI'
                         })


class OrdersAPI(generics.ListAPIView):
    class OrdersSerializer(serializers.ModelSerializer):
        class Meta:
            model = Order
            exclude = []

    serializer_class = OrdersSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        objects = Order.objects.filter(user=Profile.objects.filter(user=self.request.user).first())
        return objects


class InvoicesAPI(generics.ListAPIView):
    class InvoicesSerializer(serializers.ModelSerializer):
        class Meta:
            model = Invoice
            exclude = []

    serializer_class = InvoicesSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        objects = Invoice.objects.filter(user=Profile.objects.filter(user=self.request.user).first())
        return objects


class PaymentsAPI(generics.ListAPIView):
    class PaymentsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Payment
            exclude = []

    serializer_class = PaymentsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        objects = Payment.objects.filter(user=Profile.objects.filter(user=self.request.user).first())
        return objects


class CreditsAPI(generics.ListAPIView):
    class CreditsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Credit
            exclude = []

    serializer_class = CreditsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        objects = Credit.objects.filter(user=Profile.objects.filter(user=self.request.user).first())
        return objects


class BankPaymentInformationAPI(generics.ListAPIView):
    class BankPaymentInformationSerializer(serializers.ModelSerializer):
        class Meta:
            model = BankPaymentInformation
            exclude = []

    serializer_class = BankPaymentInformationSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        objects = BankPaymentInformation.objects.filter(user=Profile.objects.filter(user=self.request.user).first())
        return objects


class PaypalInformationAPI(generics.ListAPIView):
    class PaypalInformationSerializer(serializers.ModelSerializer):
        class Meta:
            model = PaypalInformation
            exclude = []

    serializer_class = PaypalInformationSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        objects = PaypalInformation.objects.filter(user=Profile.objects.filter(user=self.request.user).first())
        return objects
