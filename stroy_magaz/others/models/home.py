from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class HomePageText(models.Model):

    text_home_page = RichTextUploadingField(verbose_name='Текс на главной странице')
    text_home_page_2 = RichTextUploadingField(blank=True, null=True, verbose_name='Текс на главной странице 2 часть')
    


    def __str__(self):
        return str(self.text_home_page)[:15]

    class Meta:
        verbose_name = 'Тексты главной страницы'
        verbose_name_plural = 'Тексты главной страницы'



