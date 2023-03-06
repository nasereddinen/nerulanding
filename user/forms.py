from django.forms import ModelForm

from user.models import UserData


class UserDataForm(ModelForm):
    class Meta:
        model = UserData
        exclude = ['user']
