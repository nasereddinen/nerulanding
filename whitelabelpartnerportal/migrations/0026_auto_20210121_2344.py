# Generated by Django 3.1.4 on 2021-01-21 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whitelabelpartnerportal', '0025_resource_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wholesale',
            name='recurring',
            field=models.IntegerField(choices=[(1, 'One time'), (2, 'Month'), (3, 'Year')], default=1, null=True),
        ),
    ]