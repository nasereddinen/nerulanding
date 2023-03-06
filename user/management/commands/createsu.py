
from django.core.management.base import BaseCommand

from user.models import Profile, User
class Command(BaseCommand):

    help = "This command creates superuser"

    def handle(self, *args, **options):
       
        check_user = User.objects.filter(username='adminn')
        if not check_user:
            user = User.objects.create_superuser(
                'adminn', email='admin@admin.com', password='123123')
            profile = Profile(user=user)
            profile.save()
            self.stdout.write(self.style.SUCCESS(
                'Superuser created successfully'%user.name))
        else:
            self.stdout.write(self.style.WARNING(
                'Superuser already exists'))
    
  

