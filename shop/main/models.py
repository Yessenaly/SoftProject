from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='product_images' , blank = True)
    cost = models.IntegerField()
    Hot_dishes = 'Горячие блюда'
    Breakfasts = 'Завтраки'
    Smuzi = 'Смузи'
    Product = 'Продукт'
    CATEGORY_CHOICES = (
        (Hot_dishes, 'Горячие блюда'),
        (Breakfasts, 'Завтраки'),
        (Smuzi, 'Смузи'),
        (Product , 'Продукт'),
    )
    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default = Product,
    )
    def __str__(self):
        return self.name

class Programm(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    duration = models.IntegerField()
    Standart = 'Стандартная'
    For_slim = 'Для похудения'
    For_health = 'Для здорового образа жизни'
    For_vegeterians = 'Для вегетрианцев'
    Detox = 'Detox программа'
    CATEGORY_CHOICES = (
        (Standart , 'Стандартная'),
        (For_slim , 'Для похудения'),
        (For_health , 'Для здорового образа жизни'),
        (For_vegeterians , 'Для вегетрианцев'),
        (Detox , 'Detox программа'),
    )
    category = models.CharField(
        max_length = 100,
        choices = CATEGORY_CHOICES,
        default = Standart,
    )

    def __str__(self):
        return self.name