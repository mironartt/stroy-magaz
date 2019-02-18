from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse



class MainComments(models.Model):


    name_person = models.CharField(max_length=200, verbose_name='Имя того кто написал отзыв')
    email = models.CharField(max_length=200, verbose_name='Email')
    phone = models.CharField(max_length=100, blank=True, null=True, verbose_name='Телефон')
    job_satisfaction = models.IntegerField(verbose_name='Оценка')
    kind_job = models.CharField(blank=True, null=True, max_length=200, verbose_name='Какие работы производились')

    comment_body = models.TextField(blank=True, null=True, verbose_name='Тело коментария')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    moderation = models.BooleanField(default=False, verbose_name='Модерация')



    def __str__(self):
        # return 'описание: {}'.format(self.descriptions)
        return self.name_person


    class Meta:
        ordering = ('-updated',)
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'






