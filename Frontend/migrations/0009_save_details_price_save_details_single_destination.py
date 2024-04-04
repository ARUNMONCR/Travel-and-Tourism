# Generated by Django 5.0.1 on 2024-03-20 10:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0024_delete_bookings'),
        ('Frontend', '0008_alter_save_details_user_delete_userlogindb'),
    ]

    operations = [
        migrations.AddField(
            model_name='save_details',
            name='price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='save_details',
            name='single_destination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Backend.singledestinationbd'),
        ),
    ]
