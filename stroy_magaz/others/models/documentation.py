from django.db import models
# from ..validators import validate_file_extension
from ..validators import validate_file_extension
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse





class Documentation(models.Model):

    class Meta:
        ordering = ('-updated',)
        verbose_name = 'Документация'
        verbose_name_plural = 'Документация'

    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    file = models.FileField(upload_to='documentation', validators=[validate_file_extension],  verbose_name='Файл')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')


    def __str__(self):
        # return 'описание: {}'.format(self.descriptions)
        return self.title


    def get_absolute_url(self):
        return reverse('documentations_url')


