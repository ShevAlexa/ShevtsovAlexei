# Generated by Django 3.1.7 on 2021-03-16 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0017_auto_20210314_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]