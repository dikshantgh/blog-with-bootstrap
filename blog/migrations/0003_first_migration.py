# Generated by Django 3.0.5 on 2020-04-19 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_first_migration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=90),
        ),
    ]
