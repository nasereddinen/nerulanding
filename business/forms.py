from django.forms import ModelForm

from .models import BusinessCreditSteps


class BusinessCreditStepsForm(ModelForm):
    class Meta:
        model = BusinessCreditSteps
        exclude = ['user']
