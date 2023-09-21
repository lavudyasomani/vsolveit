# Generated by Django 3.2.21 on 2023-09-15 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0009_auto_20230915_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_application',
            name='gender',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job_application',
            name='address1',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='job_application',
            name='address2',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='job_application',
            name='phone_number',
            field=models.IntegerField(max_length=15),
        ),
    ]
