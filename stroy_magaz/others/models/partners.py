from django.db import models


from datetime import datetime
def generate_filename(instance, filename):
    filename = instance.name + '.jpg'
    year = datetime.now().year
    month = datetime.now().month
    return 'partners/{0}/month-{1}/{2}'.format(year, month, filename)


class Partners(models.Model):
    """Раздел сайта 'Парнеры и бренды'"""

    class Meta:
        verbose_name = 'Партнеры и бренды'
        verbose_name_plural = 'Партнеры и бренды'

    name = models.CharField(max_length=200, verbose_name='Имя партнера или бренды')
    image = models.ImageField(upload_to=generate_filename, verbose_name='Изобраение')
    link = models.CharField(max_length=200, blank=True, null=True, verbose_name='Сыллка если есть')

    def __str__(self):
        return str(self.name)[:15]

    def image_img(self):
        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

