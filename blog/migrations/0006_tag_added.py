# Generated by Django 3.0.5 on 2020-04-19 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment_added_migration'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-commented_at']},
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='tags')),
                ('tag', models.ManyToManyField(related_name='post_tags', to='blog.Post')),
            ],
        ),
    ]
