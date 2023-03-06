from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from business.models import Tier1
from core.models import BusinessTierModel
from user.models import UserData
from orders.models import UserSteps

from business import models as businessmodels

class TokenObtainPairPatchedSerializer(TokenObtainPairSerializer):
    def validate(self, instance):
        r = super(TokenObtainPairPatchedSerializer, self).validate(instance)
        r.update({
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'email': self.user.email,
        })
        return r


class NewUserSerializer(serializers.Serializer):
    email = serializers.CharField(allow_blank=False)
    password = serializers.CharField(allow_blank=False)
    first_name = serializers.CharField(allow_blank=False)
    last_name = serializers.CharField(allow_blank=False)
    phone_number = serializers.CharField(allow_blank=False)


class UserStepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSteps
        exclude = []


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        exclude = ['user', ]


class StarterVendorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = businessmodels.StarterVendorList
        exclude = []


class StoreCreditVendorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = businessmodels.StoreCreditVendorList
        exclude = []


class RevolvingBusinessCreditVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = businessmodels.RevolvingBusinessCreditVendor
        exclude = []


class NOPGSerializer(serializers.ModelSerializer):
    class Meta:
        model = businessmodels.Nopg
        exclude = []


class PersonalCreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = businessmodels.PersonalCreditCard
        exclude = []


class BusinessCreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = businessmodels.BusinessCreditCard
        exclude = []


class ShortTermLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = businessmodels.ShortTermLoan
        exclude = []


class BusinessTermLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = businessmodels.BusinessTermLoan
        exclude = []


class SBALoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = businessmodels.SbaLoan
        exclude = []


class PersonalLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = businessmodels.PersonalLoan
        exclude = []


class BusinessLinesOfCreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = businessmodels.LinesOfCredit
        exclude = []


class NoCreditCheckLoansSerializer(serializers.ModelSerializer):
    class Meta:
        model = businessmodels.NoCreditCheckLoans
        exclude = []


class InvoiceFactoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = businessmodels.InvoiceFactoring
        exclude = []


class InvoiceFinancingSerializer(serializers.ModelSerializer):
    class Meta:
        model = businessmodels.InvoiceFinancing
        exclude = []


class EquipmentFinancingSerializer(serializers.ModelSerializer):
    class Meta:
        model = businessmodels.EquipmentFinancing
        exclude = []




class TradelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessTierModel
        exclude = []
        abstract = True





class Tier1Serializer(TradelineSerializer):
    class Meta:
        model = Tier1
        exclude = []




