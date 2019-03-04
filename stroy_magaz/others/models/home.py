from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class HomePageText(models.Model):
    """
        Отображаемый текст на главной странице
        Только одна модель
    """
    class Meta:
        verbose_name = 'Тексты главной страницы (только одна модель)'
        verbose_name_plural = 'Тексты главной страницы (только одна модель)'

    text_home_page = RichTextUploadingField(verbose_name='Текс на главной странице')
    text_home_page_2 = RichTextUploadingField(blank=True, null=True, verbose_name='Текс на главной странице 2 часть')

    def __str__(self):
        return str(self.text_home_page)[:15]



