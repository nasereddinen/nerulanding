from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import *

app_name = 'yourplan'
urlpatterns = [

    url('', login_required(YourPlanView.as_view(), login_url='/user/login'),
        name='yourplan'),
]
