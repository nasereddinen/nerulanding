import random
import string

from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User

from services.StripeService import StripeService
from user.models import Profile, NewUserCredentials


class UsersService:

    @staticmethod
    def create_new_user_from_steps(self_request, request):
        if request.user.is_anonymous:
            usersteps = request.session.get('user_steps_data')
            passw = UsersService.get_random_string(8)
            Profile.objects.create_user(usersteps['email'],
                                        passw,
                                        usersteps['first_name'],
                                        usersteps['last_name'],
                                        usersteps['phone'])
            newcreds = NewUserCredentials(email=usersteps['email'], password=passw)
            newcreds.save()
            request.user = User.objects.get(email=usersteps['email'])
            auth_login(self_request, request.user)

    @staticmethod
    def get_random_string(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    @staticmethod
    def create_or_get_stripe_user(user, source=None):
        profile = Profile.objects.get(user=user)
        stripe_id = profile.stripe_id
        if not stripe_id:
            stripe_user = StripeService.create_user(
                first_name=user.first_name,
                last_name=user.last_name,
                email=user.email,
                source=source
            )
            profile.stripe_id = stripe_user['id']
            profile.save()
        else:
            stripe_user = StripeService.get_user_by_id(stripe_id)
            if source and not stripe_user['default_source']:
                StripeService.add_source_to_user(stripe_id, source)
        return stripe_user
