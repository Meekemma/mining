# Generated by Django 4.2.3 on 2023-08-11 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mining', '0013_alter_referral_balance_alter_referral_referral_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdrawal',
            name='pin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='withdrawal',
            name='wallet',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
