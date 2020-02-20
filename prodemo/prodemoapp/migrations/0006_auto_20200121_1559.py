# Generated by Django 2.2.5 on 2020-01-21 10:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prodemoapp', '0005_auto_20200120_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organisations',
            name='Organisationsp_no',
        ),
        migrations.AddField(
            model_name='organisations',
            name='Contact_pesion_First_name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='organisations',
            name='Contact_pesion_Last_name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='organisations',
            name='Organisation_mobile_number',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='organisations',
            name='createdBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='organisations',
            name='is_active',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
