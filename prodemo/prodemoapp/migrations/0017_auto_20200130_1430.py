# Generated by Django 2.2.5 on 2020-01-30 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodemoapp', '0016_auto_20200130_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
