# Generated by Django 3.0.5 on 2020-04-25 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_taggit_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dp',
            field=models.ImageField(null=True, upload_to='dp/', verbose_name='Display Image'),
        ),
    ]
