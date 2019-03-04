from django.db import models
from ..validators import validate_file_extension
from django.urls import reverse
from pytils.translit import slugify





class Order(models.Model):
    """Заказы клиентов"""

    class Meta:
        ordering = ('-updated',)
        verbose_name = 'Заказы клиентов'
        verbose_name_plural = 'Заказы клиентов'


    name_client = models.CharField(max_length=200, verbose_name='Имя клиента')
    phone_client = models.CharField(max_length=100, verbose_name='Телефон клиента')
    email_client = models.EmailField(verbose_name='Email')
    subject_work = models.CharField(max_length=200, verbose_name='Тематика работ')
    description_client = models.TextField(blank=True, null=True, verbose_name='Описание заказа клиента')

    file = models.FileField(upload_to='order_file', validators=[validate_file_extension], blank=True, null=True, verbose_name='Файл клиента')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    watched = models.BooleanField(default=False, verbose_name='Просмотрено')


    def __str__(self):
        return self.name_client

    def get_absolute_url(self):
        slug = slugify(name_client)
        return reverse('_____:_______', args=[self.slug])
