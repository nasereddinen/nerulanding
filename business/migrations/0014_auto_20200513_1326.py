# Generated by Django 3.0.5 on 2020-05-13 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0013_auto_20200507_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businesscreditcard',
            name='misc_info',
        ),
        migrations.AddField(
            model_name='businesscreditcard',
            name='max_inquiries',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='businesscreditcard',
            name='strategy',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='businesscreditcard',
            name='apr',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='businesscreditcard',
            name='bankruptcy',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='businesscreditcard',
            name='cc_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='businesscreditcard',
            name='credit_bureau',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='businesscreditcard',
            name='credit_data',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='businesscreditcard',
            name='debt_ratio',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='businesscreditcard',
            name='min_credit_score',
            field=models.CharField(max_length=50, null=True),
        ),
    ]