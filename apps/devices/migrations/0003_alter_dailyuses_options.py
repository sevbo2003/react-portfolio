# Generated by Django 4.0.4 on 2022-04-19 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_dailyuses'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dailyuses',
            options={'verbose_name': 'daily used item', 'verbose_name_plural': 'Daily uses'},
        ),
    ]