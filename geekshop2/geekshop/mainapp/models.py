from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Название', max_length=64, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Наименование продукта', max_length=128)
    description = models.TextField(verbose_name='Описание продукта', blank=True)
    image = models.ImageField(upload_to='products_img', blank=True)
    hot = models.BooleanField(verbose_name='Скидка', default=False)
    price = models.DecimalField(verbose_name='Стоимость', max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.name} ({self.category})'