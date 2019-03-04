from django.db import models
from .kindworks import KindWorks



class KindWorksComments(models.Model):
    """
        Модель Коментариев для объектов "Типы работ"
    """

    class Meta:
        ordering = ('-updated',)
        verbose_name = '''Коментарии объектов "типы работ"'''
        verbose_name_plural = '''Коментарии объектов "типы работ"'''


    parent_object = models.IntegerField(blank=True, null=True, verbose_name='ID Объектa коментирования')
    name_person = models.CharField(max_length=200, verbose_name='Имя того кто написал коментарий')
    email = models.CharField(max_length=200, verbose_name='Email')
    comment_body = models.TextField(verbose_name='Тело коментария')


    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    moderation = models.BooleanField(default=False, verbose_name='Модерация')

    watched = models.BooleanField(default=False, verbose_name='Просмотрено')

    # def get_absolte_url(self):
    #     return reverse('portfolio:p_obj_detail_url', args=[self.parent_object])

    def __str__(self):
        return self.name_person


    def obj_name(self):
        if self.parent_object:
            p_obj = KindWorks.objects.get(id=self.parent_object)
            from django.utils.safestring import mark_safe
            return mark_safe(u'{}'.format(p_obj.name))
        else:
            return '(Нет id)'

    obj_name.short_description = 'Объект коментирования'
    obj_name.allow_tags = True



class ServiceComments(models.Model):
    """
        Модель Коментариев для объектов "Предоставляемые услуги"
    """

    class Meta:
        ordering = ('-updated',)
        verbose_name = '''Коментарии объектов объектов "предоставяемые услуги"'''
        verbose_name_plural = '''Коментарии объектов объектов "предоставяемые услуги"'''


    parent_object = models.IntegerField(blank=True, null=True, verbose_name='ID Объектa коментирования')
    name_person = models.CharField(max_length=200, verbose_name='Имя того кто написал коментарий')
    email = models.CharField(max_length=200, verbose_name='Email')
    comment_body = models.TextField(verbose_name='Тело коментария')


    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    moderation = models.BooleanField(default=False, verbose_name='Модерация')

    watched = models.BooleanField(default=False, verbose_name='Просмотрено')

    # def get_absolte_url(self):
    #     return reverse('portfolio:p_obj_detail_url', args=[self.parent_object])

    def __str__(self):
        return self.name_person




    def obj_name(self):
        if self.parent_object:
            p_obj = KindWorks.objects.get(id=self.parent_object)
            from django.utils.safestring import mark_safe
            return mark_safe(u'{}'.format(p_obj.name))
        else:
            return '(Нет id)'

    obj_name.short_description = 'Объект коментирования'
    obj_name.allow_tags = True


