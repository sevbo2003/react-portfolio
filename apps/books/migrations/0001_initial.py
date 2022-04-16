# Generated by Django 4.0.4 on 2022-04-16 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'book category',
                'verbose_name_plural': 'Book Categories',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the book', max_length=300)),
                ('description', models.CharField(help_text='A little about this book', max_length=400)),
                ('status', models.CharField(choices=[('read', 'read'), ('reading', 'Reading'), ('will read', 'Read later')], max_length=10)),
                ('link', models.URLField()),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='books.bookcategory')),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'Books',
                'ordering': ('added',),
            },
        ),
    ]