# Generated by Django 2.2.5 on 2020-02-12 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prodemoapp', '0044_auto_20200212_1408'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='createdBy',
            new_name='which_Organisations',
        ),
        migrations.RenameField(
            model_name='subcategory',
            old_name='createdBy',
            new_name='which_Organisations',
        ),
    ]