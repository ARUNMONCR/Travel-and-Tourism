# Generated by Django 5.0.1 on 2024-03-11 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0017_restaurants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurants',
            name='Price',
        ),
        migrations.RemoveField(
            model_name='restaurants',
            name='Restaurants_Name',
        ),
    ]
