# Generated by Django 5.0.1 on 2024-03-01 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0002_placedb'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlightBookingDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Flight_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Depart', models.CharField(blank=True, max_length=50, null=True)),
                ('Arrive', models.CharField(blank=True, max_length=50, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Flight_Image', models.ImageField(blank=True, null=True, upload_to='image')),
            ],
        ),
    ]
