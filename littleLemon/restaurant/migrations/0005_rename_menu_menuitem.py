# Generated by Django 4.2.2 on 2023-06-20 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_alter_booking_no_of_guests'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Menu',
            new_name='MenuItem',
        ),
    ]
