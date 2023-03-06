from orders.models import UserSteps, TradelineOrder


class OrderDataService:

    @classmethod
    def get_user_steps_data(cls, user):
        user_steps = UserSteps.objects.filter(user=user)
        services = []
        for i in user_steps:
            for k in ['website', 'toll_free_number',
                      'fax_number',
                      'domain',
                      'professional_email_address']:
                status = getattr(i, k)
                if status == 2 or status == 3:
                    dash = ''
                    if k == 'website':
                        dash = "/business/website-creation-paid"
                    elif k == 'toll_free_number':
                        dash = '/business/toll-free-options/'
                    elif k == 'fax_number':
                        dash = "/business/fax-number-paid"
                    elif k == 'domain':
                        dash = getattr(i, 'domain_dashboard')
                    elif k == 'professional_email_address':
                        dash = getattr(i, 'email_provider')
                    serv = {
                        'name': k.replace('_', " "),
                        'status': 'Done' if status == 3 else 'In progress',
                        'product': getattr(i, k + '_act'),
                        'dashboard': dash
                    }
                    services.append(serv)
        return services

    @classmethod
    def get_user_tradelines_data(cls, user):
        tradelines = TradelineOrder.objects.filter(user=user)
        tradeline_data = []

        for tradeline in tradelines:
            if tradeline.which == 0 and tradeline.tradeline:
                tradeline_data.append({
                    "whitelabel_portal": tradeline.whitelabel_portal,
                    "last_purchased": tradeline.last_purchased,
                    "screenshot": tradeline.screenshot,
                    "expected_time": tradeline.expected_time,
                    "tradeline": tradeline.tradeline
                })
            elif tradeline.which == 1 and tradeline.tradeline_tier1:
                tradeline_data.append({
                    "whitelabel_portal": tradeline.whitelabel_portal,
                    "last_purchased": tradeline.last_purchased,
                    "screenshot": tradeline.screenshot,
                    "expected_time": tradeline.expected_time,
                    "tradeline": tradeline.tradeline_tier1
                })
            elif tradeline.which == 2 and tradeline.tradeline_tier2:
                tradeline_data.append({
                    "whitelabel_portal": tradeline.whitelabel_portal,
                    "last_purchased": tradeline.last_purchased,
                    "screenshot": tradeline.screenshot,
                    "expected_time": tradeline.expected_time,
                    "tradeline": tradeline.tradeline_tier2
                })
            elif tradeline.which == 3 and tradeline.tradeline_tier3:
                tradeline_data.append({
                    "whitelabel_portal": tradeline.whitelabel_portal,
                    "last_purchased": tradeline.last_purchased,
                    "screenshot": tradeline.screenshot,
                    "expected_time": tradeline.expected_time,
                    "tradeline": tradeline.tradeline_tier3
                })
            elif tradeline.which == 4 and tradeline.tradeline_tier4:
                tradeline_data.append({
                    "whitelabel_portal": tradeline.whitelabel_portal,
                    "last_purchased": tradeline.last_purchased,
                    "screenshot": tradeline.screenshot,
                    "expected_time": tradeline.expected_time,
                    "tradeline": tradeline.tradeline_tier4
                })
            elif tradeline.which == -1 and tradeline.custom_tier:
                tradeline_data.append({
                    "whitelabel_portal": tradeline.whitelabel_portal,
                    "last_purchased": tradeline.last_purchased,
                    "screenshot": tradeline.screenshot,
                    "expected_time": tradeline.expected_time,
                    "tradeline": tradeline.custom_tier
                })

        return tradeline_data
