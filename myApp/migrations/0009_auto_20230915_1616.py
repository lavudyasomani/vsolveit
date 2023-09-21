# Generated by Django 3.2.21 on 2023-09-15 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_auto_20230914_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('date', models.DateField(auto_now=True)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='img/')),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
