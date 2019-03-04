from django.db import models



from datetime import datetime
def generate_filename(instance, filename):
    filename = instance.slug + '.jpg'
    year = datetime.now().year
    month = datetime.now().month
    return 'services/gallary/{0}/month-{1}/{2}'.format(year, month, filename)



class Images(models.Model):
    """Общая галлерея изображений для раздела услуг"""

    class Meta:
        ordering = ('image',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Галлерея для всего раздела услуг'
        verbose_name_plural = '1. Галлерея для всего раздела услуг'

    image = models.ImageField(upload_to=generate_filename, verbose_name='Все изображения приложения услуги')
    name = models.CharField(max_length=200,  unique=True, verbose_name='Наименование')
    description = models.CharField(max_length=800,  blank=True, null=True, verbose_name='Описаниее')
    slug = models.SlugField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')


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
        return self.name



