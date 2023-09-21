# Generated by Django 3.2.21 on 2023-09-16 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0012_alter_job_application_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_application',
            name='address1',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='job_application',
            name='address2',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='job_application',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='job_application',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='job_application',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='job_application',
            name='image',
            field=models.ImageField(null=True, upload_to='img/'),
        ),
    ]
