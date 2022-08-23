from django.db import models
from django.db.models import Manager


class Clients(models.Model):
    name = models.CharField('Имя', max_length=20, blank=True)
    last_name = models.CharField('Фамилия', max_length=20, blank=True)
    money = models.IntegerField('Стоимость услуги', null=True)
    service = models.CharField('Услуга', max_length=30, blank=True)
    month = models.CharField('Месяц', max_length=20, blank=True)
    objects = models.Manager()
    DoesNotExist: Manager = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиента'
        verbose_name_plural = 'Клиенты'
