# Generated by Django 3.2.21 on 2023-09-16 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0015_auto_20230916_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='career',
            name='username',
        ),
    ]
