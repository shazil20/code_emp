# Generated by Django 5.0.4 on 2024-04-26 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee_management_system', '0003_remove_customuser_phone_country_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(default='user', max_length=100),
        ),
    ]