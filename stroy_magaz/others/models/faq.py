from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse



class Faq(models.Model):

    class Meta:
        verbose_name = 'FAQ/Часто задоваемые вопросы'
        verbose_name_plural = 'FAQ/Часто задоваемые вопросы'

    question = models.CharField(max_length=400, verbose_name='Вопрос')
    answer = RichTextUploadingField(verbose_name='Ответ на вопрос')

    def __str__(self):
        return self.question


    def get_absolute_url(self):
        return reverse('faq:list_faq_url')
