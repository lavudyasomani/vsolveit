# Generated by Django 3.2.21 on 2023-09-16 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0013_auto_20230916_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_application',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]
