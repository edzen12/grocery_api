from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    image = models.ImageField(upload_to="category/", blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural="Категории"


class QuantityVariant(models.Model):
    variant_name = models.CharField(max_length=100)

    def __str__(self):
        return self.variant_name
    
    class Meta:
        verbose_name_plural="Количество"


class ColorVariant(models.Model):
    color_name = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.color_name} - {self.color_code}"
    
    class Meta:
        verbose_name_plural="Цвета"


class SizeVariant(models.Model):
    size_name = models.CharField(max_length=100)

    def __str__(self):
        return self.size_name
    
    class Meta:
        verbose_name_plural="Размеры"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    price = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    stock = models.IntegerField(default=100)

    quantity_type = models.ForeignKey(QuantityVariant, blank=True, null=True, on_delete=models.PROTECT)
    color_type = models.ForeignKey(ColorVariant, blank=True, null=True, on_delete=models.PROTECT)
    size_type = models.ForeignKey(SizeVariant, blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.product_name} - {self.price} price - {self.stock} stock"
    
    class Meta:
        verbose_name_plural="Продукты"
    

class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    image = models.ImageField(upload_to="products/")

    class Meta:
        verbose_name_plural="Фото Продуктов"



