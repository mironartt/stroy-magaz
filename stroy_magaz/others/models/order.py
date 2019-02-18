from django.db import models
from ..validators import validate_file_extension
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse





class Order(models.Model):

    name_client = models.CharField(max_length=200, verbose_name='Имя клиента')
    phone_client = models.CharField(max_length=100, verbose_name='Телефон клиента')
    email_client = models.EmailField(verbose_name='Email')
    subject_work = models.CharField(max_length=200, verbose_name='Тематика работ')
    description_client = models.TextField(blank=True, null=True, verbose_name='Описание заказа клиента')

    file = models.FileField(upload_to='order_file', validators=[validate_file_extension], blank=True, null=True, verbose_name='Файл клиента')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')


    def __str__(self):
        # return 'описание: {}'.format(self.descriptions)
        return self.name_client


    class Meta:
        ordering = ('-updated',)
        verbose_name = 'Заказы клиентов'
        verbose_name_plural = 'Заказы клиентов'