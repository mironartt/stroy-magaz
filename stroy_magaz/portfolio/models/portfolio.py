from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from .images import Images



class Topic(models.Model):
    """Категории раздела портфолио"""

    class Meta:
        verbose_name = 'Категории раздела портфолио'
        verbose_name_plural = '2. Категории раздела портфолио'

    name = models.CharField(max_length=200, verbose_name='Названи категории')
    slug = models.SlugField()
    descriprion = RichTextUploadingField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio:list_p_obj_topic_url', args=[self.slug])



from datetime import datetime
def generate_filename(instance, filename):
    filename = instance.slug + '.jpg'
    year = datetime.now().year
    month = datetime.now().month
    return 'portfolio/p-obj-main-image/{0}/month-{1}/{2}'.format(year, month, filename)



class Portfolio(models.Model):
    """Оъекты раздела портфолио"""

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Портфолио'
        verbose_name_plural = '3. Объекты портфолио'

    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING, verbose_name='Категория')
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField()
    description = RichTextUploadingField(blank=True, null=True, verbose_name='Описание')
    main_image = models.ImageField(upload_to=generate_filename, verbose_name='Главное изображение')
    images = models.ManyToManyField(Images, blank=True, verbose_name='Галерея изображений')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    availability = models.BooleanField(default=True,
                                               verbose_name='Отображать на сайте')


    def get_absolute_url(self):
        return reverse('portfolio:p_obj_detail_url', args=[self.slug])


    def get_list_images(self):
        list = self.images.get_queryset()
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

    def obj_id(self):
        if self.id:
            from django.utils.safestring import mark_safe
            return mark_safe(u'{}'.format(self.id))
        else:
            return '(Нет id)'

    obj_id.short_description = 'ID объекта'
    obj_id.allow_tags = True
