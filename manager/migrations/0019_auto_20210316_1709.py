# Generated by Django 3.1.7 on 2021-03-16 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0018_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
