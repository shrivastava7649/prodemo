# Generated by Django 2.2.5 on 2020-01-17 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodemoapp', '0002_auto_20200117_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_data',
            name='Employee_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/employee_images/'),
        ),
        migrations.AlterField(
            model_name='attachments',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='media/attachments/'),
        ),
    ]
