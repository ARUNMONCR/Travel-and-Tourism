# Generated by Django 5.0.3 on 2024-03-19 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0005_save_details_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='save_details',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserloginDB',
        ),
    ]
