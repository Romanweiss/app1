from django.db import models


class Categories(models.Model):
    name = models.CharField("Название категории", max_length=150, unique=True)
    slug = models.SlugField("URL", max_length=200, unique=True, blank=True, null=True)

    class Meta:
        db_table = (
            "category"  # название таблицы, которое будет отображаться в СУБД (ед.число)
        )
        verbose_name = "категорию"  # отвечает на вопрос - кого? чего? в ед. числе
        verbose_name_plural = "Категории"  # множественное число

    
    # переопределяем метод, для адекватного отображения объектов в админке
    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField("Название", max_length=150, unique=True)
    slug = models.SlugField("URL", max_length=200, unique=True, blank=True, null=True)
    description = models.TextField("Описание", blank=True, null=True)
    image = models.ImageField(
        "Изображение", upload_to="goods_images", blank=True, null=True
    )
    price = models.DecimalField("Цена", default=0.00, max_digits=7, decimal_places=2)
    discount = models.DecimalField(
        "Скидка в процентах", default=0.00, max_digits=4, decimal_places=2
    )
    quantity = models.PositiveIntegerField("Количество", default=0)

    # Ниже связываем таблицы Categories & Products
    category = models.ForeignKey(
        to=Categories, on_delete=models.CASCADE, verbose_name="Категория"
    )

    class Meta:
        db_table = "product"
        verbose_name = "продукт"  # отвечает на вопрос - кого? чего? в ед. числе
        verbose_name_plural = "Продукты"  # множественное число


    # переопределяем метод, для адекватного отображения объектов в админке
    def __str__(self):  
        return f'{self.name} Количество - {self.quantity}'