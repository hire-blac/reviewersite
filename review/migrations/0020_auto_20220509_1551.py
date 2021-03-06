# Generated by Django 3.2.7 on 2022-05-09 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0019_alter_vote_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='reply',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
