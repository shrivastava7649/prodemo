# Generated by Django 2.2.5 on 2020-02-03 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodemoapp', '0034_auto_20200203_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='Ordr_ID',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
