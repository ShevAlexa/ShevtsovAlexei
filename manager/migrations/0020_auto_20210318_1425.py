# Generated by Django 3.1.7 on 2021-03-18 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0019_auto_20210316_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(db_index=True, help_text='ну эт тип погоняло', max_length=50, verbose_name='название'),
        ),
    ]
