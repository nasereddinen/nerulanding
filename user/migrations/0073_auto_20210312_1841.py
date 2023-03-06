from django.db import migrations

from user.models import Profile, User


# def create_user(apps, schema_editor):
#     user = User.objects.create_superuser(
#         'adminn', email='admin@admin.com', password='123123')
#     profile = Profile(user=user, created_by="admins of the web")
#     profile.save()


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0072_profile_can_see_only_created_portals'),
    ]

    operations = [
        # migrations.RunPython(create_user),

    ]
