# Generated by Django 4.0.4 on 2022-05-08 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='role',
            field=models.CharField(choices=[('Customer', 'Customer'), ('Staff', 'Staff'), ('Admin', 'Admin')], default='Customer', max_length=10),
        ),
    ]
