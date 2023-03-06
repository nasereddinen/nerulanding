from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import *

app_name = 'covid19'
urlpatterns = [
    url('homeone', login_required(HomeOneView.as_view(), login_url='/user/login'),
        name='homeone'),
    url('coronaone', login_required(CoronaOneView.as_view(), login_url='/user/login'),
        name='coronaone'),
    url('coronatwo', login_required(CoronaTwoView.as_view(), login_url='/user/login'),
        name='coronatwo'),
    url('coronathree', login_required(CoronaThreeView.as_view(), login_url='/user/login'),
        name='coronathree'),
    url('coronafour', login_required(CoronaFourView.as_view(), login_url='/user/login'),
        name='coronafour'),
    url('coronafive', login_required(CoronaFiveView.as_view(), login_url='/user/login'),
        name='coronafive'),
    url('coronasix', login_required(CoronaSixView.as_view(), login_url='/user/login'),
        name='coronasix'),
    url('coronaseven', login_required(CoronaSevenView.as_view(), login_url='/user/login'),
        name='coronaseven'),
    url('coronaeight', login_required(CoronaEightView.as_view(), login_url='/user/login'),
        name='coronaeight'),
    url('coronanine', login_required(CoronaNineView.as_view(), login_url='/user/login'),
        name='coronanine'),

]
