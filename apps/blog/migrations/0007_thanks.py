# Generated by Django 4.0.4 on 2022-05-07 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_post_body_remove_post_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thanks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'thanks',
                'verbose_name_plural': 'Thanks',
                'ordering': ['-added'],
            },
        ),
    ]
