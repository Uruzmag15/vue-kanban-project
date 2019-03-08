from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICES = (
    ('on hold', 'on hold'),
    ('in progress', 'in progress'),
    ('needs review', 'needs review'),
    ('approved', 'approved')
)

class Card(models.Model):
    creator = models.ForeignKey(User, verbose_name='Создатель', on_delete=models.CASCADE)
    status = models.CharField('Статус', max_length=100, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    text = models.TextField('Текст', max_length=500)
    date = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'