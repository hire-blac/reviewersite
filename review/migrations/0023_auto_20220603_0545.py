# Generated by Django 3.2.7 on 2022-06-03 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0022_auto_20220528_0422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='review_image1',
        ),
        migrations.RemoveField(
            model_name='review',
            name='review_image2',
        ),
        migrations.RemoveField(
            model_name='review',
            name='review_image3',
        ),
        migrations.AlterField(
            model_name='vote',
            name='value',
            field=models.CharField(choices=[('Downvote', 'Downvote'), ('Upvote', 'Upvote')], max_length=10),
        ),
        migrations.CreateModel(
            name='ReviewImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('review_image', models.ImageField(upload_to='review-images/')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_image', to='review.review')),
            ],
        ),
    ]
