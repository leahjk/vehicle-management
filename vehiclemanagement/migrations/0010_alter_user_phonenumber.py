# Generated by Django 4.0.3 on 2022-04-26 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiclemanagement', '0009_alter_vehicle_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phoneNumber',
            field=models.PositiveIntegerField(default='+254712345678', max_length=15),
        ),
    ]
