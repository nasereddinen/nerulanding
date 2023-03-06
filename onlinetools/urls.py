from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import *

app_name = 'onlinetools'
urlpatterns = [

    url('onlinetoolsone', login_required(OnlineToolsView.as_view(), login_url='/user/login'),
        name='onlinetoolsone'),
    url('onlinetoolshome', login_required(OnlineToolsHomeView.as_view(), login_url='/user/login'),
        name='onlinetoolshome'),
    url('onlinetoolstwo', login_required(OnlineToolsTwoView.as_view(), login_url='/user/login'),
        name='onlinetoolstwo'),
    url('onlinetoolsthree', login_required(OnlineToolsThreeView.as_view(), login_url='/user/login'),
        name='onlinetoolsthree'),
    url('onlinetoolsfour', login_required(OnlineToolsFourView.as_view(), login_url='/user/login'),
        name='onlinetoolsfour'),
    url('onlinetoolsfive', login_required(OnlineToolsFiveView.as_view(), login_url='/user/login'),
        name='onlinetoolsfive'),
    url('onlinetoolssix', login_required(OnlineToolsSixView.as_view(), login_url='/user/login'),
        name='onlinetoolssix'),
    url('onlinetoolsseven', login_required(OnlineToolsSevenView.as_view(), login_url='/user/login'),
        name='onlinetoolsseven'),
    url('onlinetoolseight', login_required(OnlineToolsEightView.as_view(), login_url='/user/login'),
        name='onlinetoolseight'),
    url('onlinetoolsnine', login_required(OnlineToolsNineView.as_view(), login_url='/user/login'),
        name='onlinetoolsnine'),
    url('onlinetoolsten', login_required(OnlineToolsTenView.as_view(), login_url='/user/login'),
        name='onlinetoolsten'),
    url('onlinetoolstwelve', login_required(OnlineToolsTwelveView.as_view(), login_url='/user/login'),
            name='onlinetoolstwelve'),
    url('new', login_required(NewView.as_view(), login_url='/user/login'),
            name='new'),
]
