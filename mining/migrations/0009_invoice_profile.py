# Generated by Django 4.2.3 on 2023-08-04 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mining', '0008_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mining.profile'),
        ),
    ]
