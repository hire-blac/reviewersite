# Generated by Django 3.2.7 on 2021-12-24 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0010_auto_20211218_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='category',
        ),
        migrations.AlterField(
            model_name='vote',
            name='value',
            field=models.CharField(choices=[('Downvote', 'Downvote'), ('Upvote', 'Upvote')], max_length=10),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reviewer.category')),
            ],
        ),
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reviewer.product'),
        ),
    ]
