# Generated by Django 3.2.7 on 2022-01-28 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0003_alter_vote_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='value',
            field=models.CharField(choices=[('Upvote', 'Upvote'), ('Downvote', 'Downvote')], max_length=10),
        ),
    ]
