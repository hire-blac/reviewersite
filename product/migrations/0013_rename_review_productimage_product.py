# Generated by Django 3.2.7 on 2022-06-03 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20220603_0545'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='review',
            new_name='product',
        ),
    ]
