# Generated by Django 3.2.7 on 2022-04-28 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0017_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='value',
            field=models.CharField(choices=[('Downvote', 'Downvote'), ('Upvote', 'Upvote')], max_length=10),
        ),
    ]
