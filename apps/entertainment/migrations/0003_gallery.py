# Generated by Django 4.0.4 on 2022-04-19 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainment', '0002_alter_music_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.URLField()),
                ('download_link', models.URLField()),
                ('size', models.FloatField()),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'Gallery',
                'ordering': ('-added',),
            },
        ),
    ]