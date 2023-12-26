from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=40, unique=True, verbose_name= "Логин", blank=False)
    avatar = models.ImageField(upload_to='avatars/', verbose_name="Аватар", blank=False)
    info = models.TextField(max_length=1500, verbose_name= "Информация", blank=False)

class Product(models.Model):
    release_date = models.DateTimeField(default= datetime.now)
    title = models.CharField(max_length=100, blank=False)
    info_product = models.TextField(max_length=1500, verbose_name="Описание продукта", blank=False)
    foto = models.ImageField(upload_to='foto/', verbose_name="Фотография продукта", blank=False)

class Profile(models.Model):
    username = models.ForeignKey(User, on_delete = models.CASCADE)

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    countProduct = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f' Корзина для {self.user.username} | Продукт {self.product.title}'
