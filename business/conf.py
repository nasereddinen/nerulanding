from django.conf import settings

from business.models import Lender, StoreCreditVendorList, RevolvingCredit, Nopg
from user.models import PortalGoal

portal_list = {
    "business": "",
    "fitness": "Fitness",
    "accountant": "Accountant",
    "automotive": "Automotive",
    "cannabis": "cannabis",
    "credit_repair": "credit repair",
    "ecommerce": "ecommerce",
    "hair_salon": "hair salon",
    "handy_man": "handy man",
    "insurance_agent": "insurance agent",
    "lawyer": "lawyer",
    "medical": "medical",
    "musician": "musician",
    "photography": "photography",
    "real_estate": "real estate",
    "restaurant_catering": "restaurant and catering",
    "transportation": "transportation",
    "trucking": "trucking",
    "wedding_planner": "wedding planner",
    "goals": "Goals",
    "chromeextension": "chromeextension",
    "user": "User",
    "user:business": "User",
    "construction": "construction"
}

industry_choices = (
    (1, "Electrician"),
    (2, "Gardener"),
    (3, "Tattoo Artist"),
    (4, "Photography"),
    (5, "Limo Service"),
    (6, "Nutrition Advisor"),
    (7, "Life Coach"),
    (8, "Veterinary clinic"),
    (9, "Laundromat"),
    (10, "Fitness Club"),
    (11, "Dentist"),
    (12, "Consulting"),
    (13, "Auto Repair"),
    (14, "Tutor"),
    (15, "Bakery"),
    (16, "Financial Advisor"),
    (17, "Lawyer"),
    (18, "Marketing Agency"),
    (19, "Trucking"),
    (20, "Locksmith"),
    (21, "Medical Clinic"),
    (22, "Dance Studio"),
    (23, "Carpenter"),
    (24, "Moving Company"),
    (25, "Hair Salon"),
    (26, "Cleaning Service"),
    (27, "Car Dealer"),
    (28, "Portfolio"),
    (29, "Real Estate"),
    (30, "Preschool"),
    (31, "Spa Service"),
    (32, "Physical Therapist"),
    (33, "construction"),
)


def get_business_plan_context():
    lenders = Lender.objects.all()
    store_credits = StoreCreditVendorList.objects.all()
    revolvings = RevolvingCredit.objects.all()
    nopgs = Nopg.objects.all()
    context = {
        "lenders": lenders,
        "store_credits": store_credits,
        "revolvings": revolvings,
        "nopgs": nopgs,
    }

    return context


def get_context_for_all(request, context=None):
    app_name = request.resolver_match.app_name
    if not context:
        context = {}

    context["stripe_key"] = settings.STRIPE_PUBLISHABLE_KEY

    context["verbose_portal_name"] = portal_list[app_name]
    if not hasattr(request.resolver_match, 'page_template'):
        request.resolver_match.page_template = 'pages/base-business.html'

    if request.resolver_match.app_name == 'user:business':
        request.resolver_match.page_template = 'goals/goals_base.html'
        slug = request.path.split('/my-portal-goals/')[1].split("/")[0]
        obj = PortalGoal.objects.get(slug=slug)
        context['portal_goal'] = obj
        context['portal_number'] = slug

    if request.resolver_match.app_name == 'chromeextension':
        request.resolver_match.page_template = 'base-chromeextension.html'

    return context
