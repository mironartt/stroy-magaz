from django.db import models


class MainSlider(models.Model):
    """Настройки слайдера на главной странице"""

    class Meta:
        ordering = ('serial_number',)
        verbose_name = 'Слайдер на главной странице'
        verbose_name_plural = 'Слайдер на главной странице'

    title = models.CharField(max_length=50, blank=True, null=True, verbose_name='Заголовок')
    description = models.CharField(max_length=200, blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='main_slider', verbose_name='Изображение слайда')
    button_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Название кнопки')
    button_name_coll_back = models.CharField(max_length=50, blank=True, null=True, verbose_name='Название кнопки обратного звонка')

    serial_number = models.PositiveIntegerField(default=1, verbose_name='Порядковый номер слайда')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    def __str__(self):
        return self.title

    def image_img(self):
        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True




