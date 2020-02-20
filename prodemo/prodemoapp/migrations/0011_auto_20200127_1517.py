# Generated by Django 2.2.5 on 2020-01-27 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prodemoapp', '0010_auto_20200127_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='subscription_packages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Package_Name', models.CharField(blank=True, max_length=25, null=True)),
                ('Package_Amount', models.CharField(blank=True, max_length=45, null=True)),
                ('Package_Duration', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='organisations',
            name='Organisations_Created_at',
        ),
        migrations.CreateModel(
            name='Buy_subscription_packages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activation_Start_date', models.DateField(auto_now=True)),
                ('Activation_Expired_date', models.DateField()),
                ('Amount_Status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Amount', to='prodemoapp.subscription_packages')),
                ('Package_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prodemoapp.subscription_packages')),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]