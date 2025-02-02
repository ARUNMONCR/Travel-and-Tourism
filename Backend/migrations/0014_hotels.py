# Generated by Django 5.0.1 on 2024-03-07 10:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0013_singledestinationbd_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hotel_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Hotel_Description', models.CharField(blank=True, max_length=1000, null=True)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Backend.singledestinationbd')),
            ],
        ),
    ]
