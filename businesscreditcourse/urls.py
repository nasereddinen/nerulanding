from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import *

app_name = 'businesscreditcourse'
urlpatterns = [
    url('^$', login_required(HomeView.as_view(), login_url='/user/login'),
        name='home'),
    url('^one/', login_required(OneView.as_view(), login_url='/user/login'),
        name='one'),
    url('^2/', login_required(TwoView.as_view(), login_url='/user/login'),
        name='2'),
    url('^3/', login_required(ThreeView.as_view(), login_url='/user/login'),
        name='3'),
    url('^4/', login_required(FourView.as_view(), login_url='/user/login'),
        name='4'),
    url('^5/', login_required(FiveView.as_view(), login_url='/user/login'),
        name='5'),
    url('^6/', login_required(SixView.as_view(), login_url='/user/login'),
        name='6'),
    url('^7/', login_required(SevenView.as_view(), login_url='/user/login'),
        name='7'),
    url('^8/', login_required(EightView.as_view(), login_url='/user/login'),
        name='8'),
    url('^9/', login_required(NineView.as_view(), login_url='/user/login'),
        name='9'),
    url('^10/', login_required(TenView.as_view(), login_url='/user/login'),
        name='10'),
    url('^11/', login_required(ElevenView.as_view(), login_url='/user/login'),
        name='11'),
    url('^twelve/', login_required(TwelveView.as_view(), login_url='/user/login'),
        name='twelve'),
    url('^13/', login_required(ThirteenView.as_view(), login_url='/user/login'),
        name='13'),
    url('^14/', login_required(FourteenView.as_view(), login_url='/user/login'),
        name='14'),
    url('^15/', login_required(FifteenView.as_view(), login_url='/user/login'),
        name='15'),
    url('^16/', login_required(SixteenView.as_view(), login_url='/user/login'),
        name='16'),
    url('^17/', login_required(SeventeenView.as_view(), login_url='/user/login'),
        name='17'),
    url('^18/', login_required(EighteenView.as_view(), login_url='/user/login'),
        name='18'),
    url('^19/', login_required(NineteenView.as_view(), login_url='/user/login'),
        name='19'),
    url('^20/', login_required(TwentyView.as_view(), login_url='/user/login'),
        name='20'),
    url('^21/', login_required(TwentyoneView.as_view(), login_url='/user/login'),
        name='21'),
    url('^22/', login_required(TwentytwoView.as_view(), login_url='/user/login'),
        name='22'),
    url('^23/', login_required(TwentythreeView.as_view(), login_url='/user/login'),
        name='23'),
    url('^24/', login_required(TwentyfourView.as_view(), login_url='/user/login'),
        name='24'),
    url('^25/', login_required(TwentyfiveView.as_view(), login_url='/user/login'),
        name='25'),
    url('^26/', login_required(TwentysixView.as_view(), login_url='/user/login'),
        name='26'),
    url('^27/', login_required(TwentysevenView.as_view(), login_url='/user/login'),
        name='27'),
    url('^28/', login_required(TwentyeightView.as_view(), login_url='/user/login'),
        name='28'),
    url('^29/', login_required(TwentynineView.as_view(), login_url='/user/login'),
        name='29'),
    url('^30/', login_required(ThirtyView.as_view(), login_url='/user/login'),
        name='30'),
    url('^31/', login_required(ThirtyoneView.as_view(), login_url='/user/login'),
        name='31'),
    url('^32/', login_required(ThirtytwoView.as_view(), login_url='/user/login'),
        name='32'),
]