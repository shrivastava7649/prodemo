# Generated by Django 2.2.5 on 2020-02-01 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prodemoapp', '0028_auto_20200201_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='package_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prodemoapp.Packages'),
        ),
    ]
