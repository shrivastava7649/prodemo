# Generated by Django 2.2.5 on 2020-01-30 06:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prodemoapp', '0012_auto_20200127_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Package_Type', models.CharField(choices=[('N', 'None'), ('B', 'Basic'), ('P', 'Premium'), ('Pro', 'Professional')], default='N', max_length=3)),
                ('Package_price', models.CharField(blank=True, max_length=30, null=True)),
                ('Package_Duration', models.CharField(blank=True, max_length=25, null=True)),
                ('Package_Benefits', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True, null=True)),
                ('updatedAt', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Response', models.TextField()),
                ('Ordr_ID', models.TextField()),
                ('Payment_Method', models.CharField(choices=[('A', 'NUFT'), ('B', 'CASH'), ('C', 'CHEQUE'), ('D', 'E_banking'), ('E', 'Not Listed')], default='D', max_length=3)),
                ('Amount', models.CharField(blank=True, max_length=40, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, null=True)),
                ('updatedAt', models.DateTimeField(auto_now=True, null=True)),
                ('Organisation_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prodemoapp.Organisations')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subscription_start_date', models.DateField()),
                ('Subscription_End_date', models.DateField()),
                ('Payment_status', models.CharField(choices=[('A', 'None'), ('B', 'Paid'), ('C', 'Panding'), ('D', 'Not Disclose')], default='A', max_length=3)),
                ('createdAt', models.DateTimeField(auto_now_add=True, null=True)),
                ('updatedAt', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(blank=True, default=False, null=True)),
                ('Organisation_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prodemoapp.Organisations')),
                ('Package_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prodemoapp.Packages')),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='subscription_packages',
            name='createdBy',
        ),
        migrations.DeleteModel(
            name='Buy_subscription_packages',
        ),
        migrations.DeleteModel(
            name='subscription_packages',
        ),
        migrations.AddField(
            model_name='payment',
            name='Subscription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prodemoapp.Subscription'),
        ),
        migrations.AddField(
            model_name='payment',
            name='createdBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]