# Generated by Django 3.2.7 on 2021-12-11 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0008_auto_20211211_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='value',
            field=models.CharField(choices=[('Upvote', 'Upvote'), ('Downvote', 'Downvote')], max_length=10),
        ),
    ]
