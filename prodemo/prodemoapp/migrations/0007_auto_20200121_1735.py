# Generated by Django 2.2.5 on 2020-01-21 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodemoapp', '0006_auto_20200121_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_data',
            name='is_active',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='employee_data',
            name='Employee_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
