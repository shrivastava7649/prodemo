# Generated by Django 2.2.5 on 2020-01-31 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodemoapp', '0022_organisations_logo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='Ordr_ID',
            field=models.TextField(unique=True),
        ),
    ]