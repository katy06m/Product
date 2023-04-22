from django.db import models


# Create your models here.

class Goods(models.Model):
    product = models.CharField("Наименование товара", max_length=50)
    article = models.CharField("Артикул", max_length=20)
    quantity = models.IntegerField("Количество")
    note = models.TextField("Примечание", null = True)

    def __str__(self):
        return self.product + "  " + self.article + "  " + str(self.quantity) + "  " + self.note

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"