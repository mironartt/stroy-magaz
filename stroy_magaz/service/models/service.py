from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from .images import Images
from .kindworks import KindWorks


class Unit(models.Model):
    name = models.CharField(max_length=100, verbose_name='Единица измерения')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'



from datetime import datetime
def generate_filename(instance, filename):
    filename = instance.slug + '.jpg'
    year = datetime.now().year
    month = datetime.now().month
    return 'services/service-main-image/{0}/month-{1}/{2}'.format(year, month, filename)



class Service(models.Model):
    """
        Разделс сайта "Предоставляемые услуги" (подклас типов работ)
    """

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Наименование работ (подкласс тематики работ)'
        verbose_name_plural = '3. Предоставлямемые услуги (подкласс тематики работ)'


    kindworks = models.ForeignKey(KindWorks, on_delete=models.CASCADE, verbose_name='Отношение к тематике работ')
    name = models.CharField(max_length=200, verbose_name='Наименование работ')
    slug = models.SlugField(unique=True)
    image = models.ManyToManyField(Images, blank=True, verbose_name='Галерея изображений отобрааемая в низу')
    main_image = models.ImageField(upload_to=generate_filename, blank=True, null=True,
                                   verbose_name='Главное изображение')
    desctiptions = RichTextUploadingField(blank=True, null=True, verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    price = models.CharField(max_length=50, verbose_name='Цена за 1 ед. измер', blank=True, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Единица измерения')
    gallery_availability = models.BooleanField(default=True, verbose_name='Отобраать галлерею изображений в конце страницы')

    def get_list_images(self):
        list = self.image.get_queryset()
        return list

    def __str__(self):
        return self.name

    def image_img(self):
        if self.main_image:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.main_image.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

    def get_absolute_url(self):
        return reverse('service:service_detail_url', args=[self.slug])
