import whois
from rest_framework import generics, serializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from orders.models import TradelineOrder, UserSteps
from business import models as businessmodels
from loanportal import models as loanModels
from services.OrderDataService import OrderDataService
from user import models as usermodels
from yourplan import models as yourplanModels
from . import serializers as apiserializers


class TokenObtainPairPatchedView(TokenObtainPairView):
    serializer_class = apiserializers.TokenObtainPairPatchedSerializer
    token_obtain_pair = TokenObtainPairView.as_view()


class GetUserByToken(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        user = usermodels.Profile.objects.get(user=request.user)
        plans = {
            "sezzle": yourplanModels.Sezzle,
            "klarna": yourplanModels.Klarna,
            "viabill": yourplanModels.Viabill,
            "regularpayment": yourplanModels.RegularPayment,
            "paypal": yourplanModels.Paypal,
            "quadpay": yourplanModels.Quadpay,
            "affirm": yourplanModels.Affirm,
            "behalf": yourplanModels.Behalf,
            "fundboxpay": yourplanModels.FundBoxPay,
            "invoicefactoringpayment": yourplanModels.InvoiceFactoringPayment,
            "stripe": yourplanModels.Stripe,
        }

        active_plans = []
        total_owe = 0
        financed_so_far = 0

        for i, k in plans.items():
            filter = k.objects.filter(user=user)
            if len(filter) > 0:
                plan = {
                    "name": i,
                    "how_much_owed": filter[0].how_much_owed,
                    "financed_so_far": filter[0].financed_so_far,
                }
                try:
                    total_owe += float(filter[0].how_much_owed)
                    financed_so_far += float(filter[0].financed_so_far)
                    active_plans.append(plan)
                except Exception as e:
                    print(e)
                    pass

        loans = loanModels.Loan.objects.filter(user=usermodels.Profile.objects.get(user=request.user))

        active_loans = []
        if len(loans) > 0:
            for loan in loans:
                active_loans.append({
                    'company_name': loan.company_name,
                    'interest_rate': loan.interest_rate,
                    'term_length': loan.term_length,
                })

        return Response({
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'total_owe': total_owe,
            'financed_so_far': financed_so_far,
            'active_plans': active_plans,
            'active_loans': active_loans,
        })


class FetchPersonalData(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            data = usermodels.UserData.objects.get(user=usermodels.Profile.objects.get(user=request.user))
            return Response(apiserializers.UserDataSerializer().to_representation(data))
        except usermodels.UserData.DoesNotExist:
            return Response({
                'message': 'No data in database',
            })
        except Exception as e:
            return Response({
                'message': 'error',
                'type': str(type(e)),
            })


class RegisterNewUserAPI(generics.GenericAPIView):
    serializer_class = apiserializers.NewUserSerializer

    def post(self, request, *args, **kwargs):
        try:
            userr = self.get_serializer(data=request.data)
            if userr.is_valid():
                usermodels.Profile.objects.create_user(request.data['email'],
                                                       request.data['password'],
                                                       request.data['first_name'],
                                                       request.data['last_name'],
                                                       request.data['phone_number'])
                return Response({'message': 'success'}, status=200)
            else:
                raise Exception("Form is not valid.")
        except Exception as e:
            return Response({'message': f'{e}'}, status=403)


class StarterVendorListAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.StarterVendorListSerializer
    queryset = businessmodels.StarterVendorList.objects.all()
    permission_classes = (IsAuthenticated,)


class StoreCreditVendorListAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.StoreCreditVendorListSerializer
    queryset = businessmodels.StoreCreditVendorList.objects.all()
    permission_classes = (IsAuthenticated,)


class RevolvingBusinessCreditVendorAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.RevolvingBusinessCreditVendorSerializer
    queryset = businessmodels.RevolvingBusinessCreditVendor.objects.all()
    permission_classes = (IsAuthenticated,)


class NOPGAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.NOPGSerializer
    queryset = businessmodels.Nopg.objects.all()
    permission_classes = (IsAuthenticated,)


class PersonalCreditCardAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.PersonalCreditCardSerializer
    queryset = businessmodels.PersonalCreditCard.objects.all()
    permission_classes = (IsAuthenticated,)


class BusinessCreditCardAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.BusinessCreditCardSerializer
    queryset = businessmodels.BusinessCreditCard.objects.all()
    permission_classes = (IsAuthenticated,)


class ShortTermLoanAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.ShortTermLoanSerializer
    queryset = businessmodels.ShortTermLoan.objects.all()
    permission_classes = (IsAuthenticated,)


class BusinessTermLoanAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.BusinessTermLoanSerializer
    queryset = businessmodels.BusinessTermLoan.objects.all()
    permission_classes = (IsAuthenticated,)


class SBALoanAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.SBALoanSerializer
    queryset = businessmodels.SbaLoan.objects.all()
    permission_classes = (IsAuthenticated,)


class PersonalLoanAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.PersonalLoanSerializer
    queryset = businessmodels.PersonalLoan.objects.all()
    permission_classes = (IsAuthenticated,)


class BusinessLinesOfCreditAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.BusinessLinesOfCreditSerializer
    queryset = businessmodels.LinesOfCredit.objects.all()
    permission_classes = (IsAuthenticated,)


class NoCreditCheckLoansAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.NoCreditCheckLoansSerializer
    queryset = businessmodels.NoCreditCheckLoans.objects.all()
    permission_classes = (IsAuthenticated,)


class InvoiceFactoringAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.InvoiceFactoringSerializer
    queryset = businessmodels.InvoiceFactoring.objects.all()
    permission_classes = (IsAuthenticated,)


class InvoiceFinancingAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.InvoiceFinancingSerializer
    queryset = businessmodels.InvoiceFinancing.objects.all()
    permission_classes = (IsAuthenticated,)


class EquipmentFinancingAPI(viewsets.ModelViewSet):
    serializer_class = apiserializers.EquipmentFinancingSerializer
    queryset = businessmodels.EquipmentFinancing.objects.all()
    permission_classes = (IsAuthenticated,)


class GetUserStepsAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            steps = UserSteps.objects.filter(user=request.user).first()

            # steps_serialized = apiserializers.UserStepsSerializer().to_representation(steps)
            return Response({
                'website': steps.website,
                'toll_free': steps.toll_free_number,
                'fax_number': steps.fax_number,
                'domain': steps.domain,
                'professional_email': steps.professional_email_address,
            })

            # return Response(steps_serialized, status=200)

        except UserSteps.DoesNotExist:
            return Response({
                'website': 1,
                'toll_free': 1,
                'fax_number': 1,
                'domain': 1,
                'professional_email': 1,
            })

        except Exception as e:
            return Response({'message': f'{e}'}, status=403)


class uploadLoanDocument(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        return Response({
            'message': 'good'
        })


class checkDomainApi(APIView):
    def post(self, request):
        try:
            print(request.POST)
            domain = request.POST['domain']
            domain = domain.replace("www.", "").replace("http://", "").replace("https://", "")
            if not len(domain) > 0:
                raise ValueError('Domain can not be empty')
            if '.' not in domain:
                raise ValueError('Wrong domain format')
            try:
                domainData = whois.whois(domain)
            except whois.parser.PywhoisError:
                domainData = None

            if not domainData:
                return Response({
                    'status': 'true'
                }, 200)
            else:
                return Response({
                    'status': 'false',
                    'error': f"domain {domain} is already taken."
                }, 200)

        except Exception as e:
            return Response({
                'status': 'false',
                'error': str(e)
            }, 200)


class TradelinesAPI(APIView):
    class TradelinesSerializer(serializers.Serializer):
        class Meta:
            model = TradelineOrder
            exclude = ['user']

        tradeline = serializers.CharField(source='tradeline.business_name')

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        tradelines = TradelineOrder.objects.filter(user=request.user)
        response = []

        for i in tradelines:
            if i.which == 0:
                tr = i.tradeline
            elif i.which == 1:
                tr = i.tradeline_tier1
            elif i.which == 2:
                tr = i.tradeline_tier2
            elif i.which == 3:
                tr = i.tradeline_tier3
            elif i.which == 4:
                tr = i.tradeline_tier4
            elif i.which == -1:
                tr = i.custom_tier
            else:
                continue

            response.append({
                "company_name": tr.company_name,
                "product": tr.product,
                "tradeline_amount": tr.tradeline_amount,
                "price": tr.price,
                "charge": tr.charge
            })


        return Response(response)



