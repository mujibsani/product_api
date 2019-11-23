from django.db import models
from django.utils.text import slugify


class Products(models.Model):
    product_name = models.CharField(max_length=50)
    product_code = models.CharField(max_length=20)
    product_slug = models.SlugField(
        default='',
        editable=False,
        max_length=200,
    )

    def save(self, *args, **kwargs):
        value = self.product_name + self.product_code
        self.product_slug = slugify(value, allow_unicode=True)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name


class ProductAttribute(models.Model):
    product = models.ForeignKey(Products, related_name='product_attribute', on_delete=models.CASCADE)
    product_color = models.CharField(max_length=20)
    product_size = models.CharField(max_length=10)

    def __str__(self):
        return self.product_color + ' ' + self.product_size


class ProductPrice(models.Model):
    product = models.ForeignKey(Products, related_name='product', on_delete=models.CASCADE)
    product_attribute = models.ForeignKey(ProductAttribute, related_name='product_attribute', on_delete=models.CASCADE)
    product_price = models.CharField(max_length=15)

    class Meta:
        unique_together = ("product_attribute", "product")

    def __int__(self):
        return self.id