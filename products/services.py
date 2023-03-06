def create_usersteps_for_subdomain(subdomain):
    from products.models import UserStepsProduct, available_user_steps
    from dynamic.models import Subdomain
    try:
        subdomain = Subdomain.objects.get(sub_name=subdomain)

        existing_steps = UserStepsProduct.objects.filter(whitelabel_portal__sub_name=subdomain)

        for user_step, data in available_user_steps.items():
            if not existing_steps.filter(name=user_step).exists():
                new_step = UserStepsProduct(name=user_step, price=data[0], recurring=data[1],
                                            whitelabel_portal=subdomain)
                new_step.save()

    except Exception as e:
        print(e)


def create_tradelines_for_subdomain(subdomain):
    from products.models import Tradelines
    from dynamic.models import Subdomain
    try:
        subdomain = Subdomain.objects.get(sub_name=subdomain)
        tradelines = Tradelines.objects.filter(whitelabel_portal=None)
        existing_tradelines = Tradelines.objects.filter(whitelabel_portal__sub_name=subdomain)

        for new_tradeline in tradelines:
            if not existing_tradelines.filter(product=new_tradeline.product,
                                              company_name=new_tradeline.company_name).exists():
                new_tradeline.pk = None
                new_tradeline.product_id = None
                new_tradeline.whitelabel_portal = subdomain
                new_tradeline.save()

    except Exception as e:
        print(e)
