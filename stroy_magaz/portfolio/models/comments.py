from django.db import models
from django.urls import reverse

from .portfolio import Portfolio



class PortfolioComments(models.Model):
    """
        Модель Коментариев для объектов портфолио
    """

    parent_object = models.IntegerField(blank=True, null=True, verbose_name='ID Объектa коментирования')
    name_person = models.CharField(max_length=200, verbose_name='Имя того кто написал коментарий')
    email = models.CharField(max_length=200, verbose_name='Email')
    comment_body = models.TextField(verbose_name='Тело коментария')


    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    moderation = models.BooleanField(default=False, verbose_name='Модерация')

    # def get_absolte_url(self):
    #     return reverse('portfolio:p_obj_detail_url', args=[self.parent_object])

    def __str__(self):
        # return 'описание: {}'.format(self.descriptions)
        return self.name_person


    class Meta:
        ordering = ('-updated',)
        verbose_name = 'Коментарии объектов портфолио'
        verbose_name_plural = 'Коментарии объектов портфолио'



    def obj_name(self):
        if self.parent_object:
            p_obj = Portfolio.objects.get(id=self.parent_object)
            from django.utils.safestring import mark_safe
            return mark_safe(u'{}'.format(p_obj.name))
        else:
            return '(Нет id)'

    obj_name.short_description = 'Объект коментирования'
    obj_name.allow_tags = True


