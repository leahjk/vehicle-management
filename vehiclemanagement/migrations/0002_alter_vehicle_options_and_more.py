# Generated by Django 4.0.3 on 2022-03-16 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiclemanagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicle',
            options={'ordering': ['-yearofmanufacture'], 'verbose_name': 'Vehicle', 'verbose_name_plural': 'Vehicles'},
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='yearmanufacture',
            new_name='yearofmanufacture',
        ),
    ]
