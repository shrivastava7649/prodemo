# Generated by Django 2.2.5 on 2020-01-31 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodemoapp', '0024_auto_20200131_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='Ordr_ID',
            field=models.TextField(unique=True),
        ),
    ]
