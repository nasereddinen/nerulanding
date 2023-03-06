from django.test import SimpleTestCase ,TestCase
from django.urls import reverse , resolve
from .views import *

class TestUrls(SimpleTestCase):

    def test_business_user_view_url(self):
        url = reverse('business:user_data')
        self.assertEquals(resolve(url).func.view_class,UserDataView)

    def test_business_card_view_url(self):
        url = reverse('business:virtual_card')
        self.assertEquals(resolve(url).func.view_class,VirtualCardView)

    def test_business_credit_affiliate_view_url(self):
        url = reverse('business:credit-affiliate')
        self.assertEquals(resolve(url).func.view_class,CreditAffiliate)

    def test_business_upgrade_view_url(self):
        url = reverse('business:upgrade')
        self.assertEquals(resolve(url).func.view_class,UpgradeView)

    def test_business_goal_view_url(self):
        url = reverse('business:goals')
        self.assertEquals(resolve(url).func.view_class,GoalView)

    def test_business_life_goal_view_url(self):
        url = reverse('business:lifegoals')
        self.assertEquals(resolve(url).func.view_class,LifeGoalView)

    def test_business_restricted_view_url(self):
        url = reverse('business:restricted')
        self.assertEquals(resolve(url).func.view_class,RestrictedView)

    def test_business_financing_view_url(self):
        url = reverse('business:financing')
        self.assertEquals(resolve(url).func.view_class,FinancingView)

    def test_business_financing_plan_1_view_url(self):
        url = reverse('business:financing_plan_1')
        self.assertEquals(resolve(url).func.view_class,FinancingPlan1View)

    def test_business_financing_plan_2_view_url(self):
        url = reverse('business:financing_plan_2')
        self.assertEquals(resolve(url).func.view_class,FinancingPlan2View)

    def test_business_financing_plan_3_view_url(self):
        url = reverse('business:financing_plan_3')
        self.assertEquals(resolve(url).func.view_class,FinancingPlan3View)

    def test_business_financing_plan_6_view_url(self):
        url = reverse('business:financing_plan_6')
        self.assertEquals(resolve(url).func.view_class,FinancingPlan6View)

    def test_business_financing_plan_7_view_url(self):
        url = reverse('business:financing_plan_7')
        self.assertEquals(resolve(url).func.view_class,FinancingPlan7View)

    def test_business_financing_plan_8_view_url(self):
        url = reverse('business:financing_plan_8')
        self.assertEquals(resolve(url).func.view_class,FinancingPlan8View)

    def test_business_financing_plan_10_view_url(self):
        url = reverse('business:financing_plan_10')
        self.assertEquals(resolve(url).func.view_class,FinancingPlan10View)

    def test_business_financing_plan_12_view_url(self):
        url = reverse('business:financing_plan_12')
        self.assertEquals(resolve(url).func.view_class,FinancingPlan12View)

    def test_business_financing_plan_15_view_url(self):
        url = reverse('business:financing_plan_15')
        self.assertEquals(resolve(url).func.view_class,FinancingPlan15View)
