# Generated by Django 5.0.1 on 2024-03-06 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0007_singledestinationbd_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleDes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]