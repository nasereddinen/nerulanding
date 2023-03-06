from django.forms.models import model_to_dict
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from business.models import CredibilitySteps, OtherChecklistSteps, Tier1, Tier2, Tier3, Tier4
from dynamic.models import Subdomain
from products.models import Tradelines
from restapi.serializers import TradelineSerializer, Tier1Serializer
from services.OrderDataService import OrderDataService


class StepsChecklistAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        steps = CredibilitySteps.objects.filter(user=request.user).first()
        if not steps:
            steps = CredibilitySteps(user=request.user)
            steps.save()

        othersteps = OtherChecklistSteps.objects.filter(user=request.user).first()
        if not othersteps:
            othersteps = OtherChecklistSteps(user=request.user)
            othersteps.save()

        steps_done = True
        for i, k in steps.__dict__.items():
            if not bool(k):
                steps_done = False

        return Response({'steps_done': steps_done, 'othersteps': model_to_dict(othersteps)})

    def post(self, request):
        data = request.data
        othersteps = OtherChecklistSteps.objects.filter(user=request.user).first()
        if not othersteps:
            othersteps = OtherChecklistSteps(user=request.user)
            othersteps.save()

        if 'established' in data:
            othersteps.established = data.get('established')
        othersteps.save()
        print(data)

        return Response({'status': 'ok'})


class StepsChecklistCredibilityAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        steps = CredibilitySteps.objects.filter(user=request.user).first()
        if not steps:
            steps = CredibilitySteps(user=request.user)
            steps.save()

        return Response({'steps': model_to_dict(steps)})

    def post(self, request):

        data = request.data

        steps = CredibilitySteps.objects.filter(user=request.user).first()
        if not steps:
            steps = CredibilitySteps(user=request.user)
            steps.save()

        if 'businessName' in data:
            steps.business_name = data.get('businessName')
        if 'businessAddress' in data:
            steps.business_address = data.get('businessAddress')
        if '2' in data:
            steps.entity = data.get('2')
        if '3' in data:
            steps.ein = data.get('3')
        if '4' in data:
            steps.four11 = data.get('4')
        if '5' in data:
            steps.website = data.get('5')
        if '6' in data:
            steps.email = data.get('6')
        if '7' in data:
            steps.license = data.get('7')
        if '8' in data:
            steps.bankaccount = data.get('8')
        if '9' in data:
            steps.merchant = data.get('9')

        steps.save()
        print(data)
        return Response({'status': 'ok'})


class BusinessCreditBuilderTrackerAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        tier1 = Tier1Serializer(Tier1.objects.all(), many=True).data
        tier2 = Tier1Serializer(Tier2.objects.all(), many=True).data
        tier3 = Tier1Serializer(Tier3.objects.all(), many=True).data
        tier4 = Tier1Serializer(Tier4.objects.all(), many=True).data

        subdomain = Subdomain.objects.filter(sub_name=request.host.name).first()
        our_tradelines = Tradelines.objects.filter(whitelabel_portal__sub_name=subdomain)

        our_tradelines = Tier1Serializer(our_tradelines, many=True).data

        current_tradelines = OrderDataService.get_user_tradelines_data(request.user)
        tradeline_count = len(current_tradelines)
        return Response({
                          # "tradeline_count": tradeline_count,
                          "currentAmount": tradeline_count,
                          "tier1": tier1,
                          "tier2": tier2,
                          "tier3": tier3,
                          "tier4": tier4,
                          "offeredTradelines": our_tradelines
                      })
