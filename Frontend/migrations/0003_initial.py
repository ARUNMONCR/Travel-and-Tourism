# Generated by Django 5.0.1 on 2024-02-28 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Frontend', '0002_delete_userlogindb'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserloginDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('User', models.CharField(blank=True, max_length=50, null=True)),
                ('Password', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
