# Generated by Django 3.2.19 on 2023-07-30 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20230730_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='num_comment',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='newuser',
            name='num_like',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='newuser',
            name='num_post',
            field=models.IntegerField(default=0),
        ),
    ]
