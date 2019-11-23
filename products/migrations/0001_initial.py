# Generated by Django 2.2.7 on 2019-11-23 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_code', models.CharField(max_length=20)),
                ('product_slug', models.SlugField(default='', editable=False, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_color', models.CharField(max_length=20)),
                ('product_size', models.CharField(max_length=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_attribute', to='products.Products')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_price', models.CharField(max_length=15)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.Products')),
                ('product_attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_attribute', to='products.ProductAttribute')),
            ],
            options={
                'unique_together': {('product_attribute', 'product')},
            },
        ),
    ]
