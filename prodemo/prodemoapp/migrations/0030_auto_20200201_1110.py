# Generated by Django 2.2.5 on 2020-02-01 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodemoapp', '0029_payment_package_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='is_active',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='Subscription_days',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='Subscription_End_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
