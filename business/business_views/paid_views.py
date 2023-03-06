from django.shortcuts import render, redirect
from django.views import View

from business.conf import get_context_for_all, industry_choices
from business.forms import BusinessCreditStepsForm
from dynamic.models import Subdomain
from orders.models import UserSteps
from products.models import Tradelines, UserStepsProduct
from services.ModelServices import check_all_required_fields_filled
from user.forms import UserDataForm
from user.models import Profile, UserData
from django.forms.models import model_to_dict




class ExternalCredentialsView(View):
    def get(self, request):

        creds = request.user.external_resources.all()
        print(creds)

        return render(request, "external_credentials.html", {"creds": creds})

