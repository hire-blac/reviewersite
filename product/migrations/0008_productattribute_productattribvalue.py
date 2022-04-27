# Generated by Django 3.2.7 on 2022-04-27 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.ManyToManyField(related_name='attrbCategory', to='product.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAttribValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Valueproduct', to='product.product')),
                ('productAttribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attribute', to='product.productattribute')),
            ],
        ),
    ]
