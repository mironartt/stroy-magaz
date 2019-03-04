from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from .images import Images


from datetime import datetime
def generate_filename(instance, filename):
    filename = instance.slug + '.jpg'
    year = datetime.now().year
    month = datetime.now().month
    return 'services/kindwork-main-image/{0}/month-{1}/{2}'.format(year, month, filename)


class KindWorks(models.Model):
    """Модель типов предоставляемых работ"""

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Тематика работ'
        verbose_name_plural = '2. Тематика работ'

    name = models.CharField(max_length=200, verbose_name='Тематика работ')
    slug = models.SlugField()
    intro = models.CharField(max_length=200, blank=True, null=True, verbose_name='Краткое описание')
    main_image = models.ImageField(upload_to=generate_filename, blank=True, null=True, verbose_name='Главное изображение')
    desctiption = RichTextUploadingField(blank=True, null=True, verbose_name='Описание производимы работ')
    image = models.ManyToManyField(Images, blank=True, verbose_name='Галерея изображений отображаемая в низу')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    gallery_availability = models.BooleanField(default=False,
                                               verbose_name='Отобраать галлерею изображений в конце страницы')

    def __str__(self):
        return self.name


    def get_list_images(self):
        list = self.image.get_queryset()
        return list

    def image_img(self):
        if self.main_image:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.main_image.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True


    def get_absolute_url(self):
        return reverse('service:kind_works_detail_url', args=[self.slug])


    def obj_id(self):
        if self.id:
            from django.utils.safestring import mark_safe
            return mark_safe(u'{}'.format(self.id))
        else:
            return '(Нет id)'

    obj_id.short_description = 'ID объекта'
    obj_id.allow_tags = True


