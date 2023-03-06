from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import *
from business.urls import urlpatterns as business_urls

app_name = 'goals'

urlpatterns = [
    url('repairbusinesscredit/', login_required(RepairBusinessCreditView.as_view(), login_url='/user/login'), name='repairbusinesscredit'),
    url('repairbusinesscredit_1', login_required(RepairBusinessCreditViewOne.as_view(), login_url='/user/login'), name='repairbusinesscredit1'),

    url('offeringfinancing/', login_required(OfferingFinancingView.as_view(), login_url='/user/login'), name='offeringfinancing'),

    url('merchant/', login_required(MerchantView.as_view(), login_url='/user/login'), name='merchant'),

    url('makeextramoney/', login_required(MakeExtraMoneyView.as_view(), login_url='/user/login'), name='makeextramoney'),

    url('marketingbusiness/', login_required(MarketingBusinessView.as_view(), login_url='/user/login'), name='marketingbusiness'),

    url('immediatemoney/', login_required(ImmediateMoneyView.as_view(), login_url='/user/login'), name='immediatemoney'),
    url('immediatemoney/1', login_required(ImmediateMoneyViewOne.as_view(), login_url='/user/login'), name='immediatemoney1'),
    url('immediatemoney/2', login_required(ImmediateMoneyViewTwo.as_view(), login_url='/user/login'), name='immediatemoney2'),

    url('buildbusinesscredit/', login_required(BuildBusinessCreditView.as_view(), login_url='/user/login'), name='buildbusinesscredit'),
    url('buildbusinesscredit_1', login_required(BuildBusinessCreditViewOne.as_view(), login_url='/user/login'), name='buildbusinesscredit1'),
    url('buildbusinesscredit_2', login_required(BuildBusinessCreditViewTwo.as_view(), login_url='/user/login'), name='buildbusinesscredit2'),
    url('buildbusinesscredit_3', login_required(BuildBusinessCreditViewThree.as_view(), login_url='/user/login'), name='buildbusinesscredit3'),
    url('buildbusinesscredit_4', login_required(BuildBusinessCreditViewFour.as_view(), login_url='/user/login'), name='buildbusinesscredit4'),
    url('buildbusinesscredit_5', login_required(BuildBusinessCreditViewFive.as_view(), login_url='/user/login'), name='buildbusinesscredit5'),
    url('buildbusinesscredit_6', login_required(BuildBusinessCreditViewSix.as_view(), login_url='/user/login'), name='buildbusinesscredit6'),
    url('buildbusinesscredit_7', login_required(BuildBusinessCreditViewSeven.as_view(), login_url='/user/login'), name='buildbusinesscredit7'),

    url('buildpersonalcredit/', login_required(BuildPersonalCreditView.as_view(), login_url='/user/login'), name='buildpersonalcredit'),
    url('buildpersonalcredit_1', login_required(BuildPersonalCreditViewOne.as_view(), login_url='/user/login'), name='buildpersonalcredit1'),
    url('buildpersonalcredit_2', login_required(BuildPersonalCreditViewTwo.as_view(), login_url='/user/login'), name='buildpersonalcredit2'),
    url('buildpersonalcredit_3', login_required(BuildPersonalCreditViewThree.as_view(), login_url='/user/login'), name='buildpersonalcredit3'),

] + business_urls[:-1]
