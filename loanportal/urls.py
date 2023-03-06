from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import *

app_name = 'loanportal'
urlpatterns = [

    url('loanapplication', login_required(LoanApplicationView.as_view(), login_url='/user/login'),
        name='loanapplication'),
    url('loanoffers', login_required(LoanOffersView.as_view(), login_url='/user/login'),
        name='loanoffers'),
    url('', login_required(LoanOffersView.as_view(), login_url='/user/login'),
        name='loanoffers'),
]
