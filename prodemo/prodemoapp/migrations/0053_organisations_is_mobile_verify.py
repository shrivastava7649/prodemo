# Generated by Django 2.2.5 on 2020-02-18 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodemoapp', '0052_organisations_org_uni_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisations',
            name='is_mobile_verify',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
