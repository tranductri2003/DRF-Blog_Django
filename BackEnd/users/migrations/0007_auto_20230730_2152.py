# Generated by Django 3.2.19 on 2023-07-30 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20230730_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='num_comment',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='num_like',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='num_post',
        ),
    ]
