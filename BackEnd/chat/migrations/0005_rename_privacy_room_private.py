# Generated by Django 4.2.4 on 2023-08-16 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_room_participants_room_privacy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='privacy',
            new_name='private',
        ),
    ]
