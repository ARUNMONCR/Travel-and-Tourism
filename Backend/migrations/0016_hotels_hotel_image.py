# Generated by Django 5.0.1 on 2024-03-07 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0015_singledestinationbd_placename'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='Hotel_image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
