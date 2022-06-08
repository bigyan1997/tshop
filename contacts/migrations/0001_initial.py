# Generated by Django 4.0.4 on 2022-05-04 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('email', models.EmailField(db_index=True, max_length=50, unique=True)),
                ('subject', models.CharField(db_index=True, max_length=50)),
                ('message', models.TextField(db_index=True, max_length=9999)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('replied', models.BooleanField(default=False)),
            ],
        ),
    ]
