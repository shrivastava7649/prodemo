# Generated by Django 2.2.5 on 2020-02-18 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodemoapp', '0051_organisations_admin_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisations',
            name='org_uni_id',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
