# Generated by Django 4.0.4 on 2022-05-06 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entertainment', '0004_music_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='length',
        ),
    ]
