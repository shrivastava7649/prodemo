# Generated by Django 2.2.5 on 2020-01-23 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodemoapp', '0008_auto_20200123_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisations',
            name='otp_forgot_password',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
