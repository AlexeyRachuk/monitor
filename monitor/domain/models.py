from datetime import date
from django.db import models


class DomainPage(models.Model):
    title = models.CharField('Домен', max_length=255)
    create_date = models.DateField('Дата окончания', null=True, blank=True)
    now_date = models.DateField(default=date.today)
    draft = models.BooleanField('Публикация', default=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Домены"
        verbose_name_plural = "Домены"
