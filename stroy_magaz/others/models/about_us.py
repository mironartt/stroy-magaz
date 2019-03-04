from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse



class AboutUs(models.Model):
    """
        Информация о владельце и сайте
    """
    class Meta:
        verbose_name = 'Тексты страницы о компании и контакты (только одна модель)'
        verbose_name_plural = 'Тексты страницы о компании и контакты (только одна модель)'

    text_about_us_page = RichTextUploadingField(verbose_name='Текс на странице "О нас"')
    text_about_us_page_2 = RichTextUploadingField(blank=True, null=True, verbose_name='Текс на странице "Контакты"')
    phone = models.CharField(max_length=50, blank=True, null=True, verbose_name='Телефон компании (отображается в шапке сайта)')
    address = models.CharField(max_length=200, blank=True, null=True, verbose_name='Адрес компании (отображается в шапке сайта)')
    time_work = models.CharField(max_length=200, blank=True, null=True, verbose_name='Время работы компании (отображается в низу сайта и странице "Контакты")')
    email = models.EmailField(blank=True, null=True, verbose_name='Email компании (отображается в шапке сайта)')
    smal_company_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Сокрощенное наименование компании (отображается в шапке сайта)')
    discription_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Описание навания на главную (отображается под сокращенным назаванием компании)')
    title_notes = models.TextField(blank=True, null=True, verbose_name='Заголовок примечаний, в футере')
    notes = models.TextField(blank=True, null=True, verbose_name='Примечания, в футере')

    full_company_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Полное наименование компании')
    fio_entrepreneur = models.CharField(max_length=200, blank=True, null=True, verbose_name='ФИО предпринимателя')
    ip_registration_address = models.CharField(max_length=200, blank=True, null=True, verbose_name='Адрес регистрации ИП')
    inn_kpp = models.CharField(max_length=200, blank=True, null=True, verbose_name='ИНН')
    bin = models.CharField(max_length=200, blank=True, null=True, verbose_name='ОГРНИП')
    okved = models.CharField(max_length=200, blank=True, null=True, verbose_name='ОКВЭД')
    okpo = models.CharField(max_length=200, blank=True, null=True, verbose_name='ОКПО')
    requisites = models.TextField(blank=True, null=True, verbose_name='Банковские реквизиты')
    self_phone = models.CharField(max_length=200, blank=True, null=True, verbose_name='Контактный телефон')
    self_email = models.CharField(max_length=200, blank=True, null=True, verbose_name='Электронная почта')

    def __str__(self):
        return 'Название: {}'.format(self.smal_company_name)

    def get_absolute_url(self):
        return reverse('about_us_url')



