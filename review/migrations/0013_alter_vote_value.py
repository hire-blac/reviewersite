# Generated by Django 3.2.7 on 2022-03-19 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0012_alter_vote_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='value',
            field=models.CharField(choices=[('Downvote', 'Downvote'), ('Upvote', 'Upvote')], max_length=10),
        ),
    ]
