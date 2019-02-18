from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class CollBackClient(models.Model):

    name_client = models.CharField(max_length=200, verbose_name='Имя клиента')
    phone_client = models.CharField(max_length=100, verbose_name='Телефон клиента')
    coll_time = models.CharField(max_length=300, verbose_name='Время обратного звонка')
    description_client = models.TextField(blank=True, null=True, verbose_name='Описание клиента')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')


    def __str__(self):
        # return 'описание: {}'.format(self.descriptions)
        return self.name_client


    class Meta:
        ordering = ('-updated',)
        verbose_name = 'Заказ клиента на звонок'
        verbose_name_plural = 'Заказ клиента на звонок'



class CollBack(models.Model):

    title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Заголовок')
    description = models.CharField(max_length=500, blank=True, null=True, verbose_name='Описание')
    description_short = models.CharField(max_length=200, blank=True, null=True, verbose_name='Описание короткое')
    btn_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Имя кнопки')
    image = models.ImageField(upload_to='coll_back', blank=True, null=True, verbose_name='Изображение')
    avalible = models.BooleanField(default=True, verbose_name='Доступность обратного звонка')





    def image_img(self):
        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True



    def __str__(self):
        # return 'описание: {}'.format(self.descriptions)
        return self.title


    class Meta:

        verbose_name = 'Настройки страницы заказа обратного звонка'
        verbose_name_plural = 'Настройки страницы заказа обратного звонка'
