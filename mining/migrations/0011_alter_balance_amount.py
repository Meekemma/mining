# Generated by Django 4.2.3 on 2023-08-05 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mining', '0010_balance_deposit_balance_withdrawal_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
