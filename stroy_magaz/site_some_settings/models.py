from django.db import models



class SiteSettings(models.Model):
    """
    Модель управление некоторыми настройками сайта
    """

    class Meta:
        # ordering = ('name',)
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'

    site_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Название сайта отобраается в название вкладки')
    confirm_main_comments = models.BooleanField(default=False,
                                                     verbose_name="""Публикация отзывов в разделе "отзывы" без модерации""")
    confirm_portfolio_comments = models.BooleanField(default=False, verbose_name='Публикация коментариев в разделе портфолио без модерации')

    confirm_services_comments = models.BooleanField(default=False,
                                                     verbose_name='Публикация коментариев в разделе "типы работ и усуи" без модерации')

    avalible_load_files_order = models.BooleanField(default=True,
                                                     verbose_name='Разрешить клиентам загружать файлы на сервер')


    social_link_vk = models.URLField(blank=True, null=True, verbose_name='Сылка на профиль ВК')
    social_link_youtube = models.URLField(blank=True, null=True, verbose_name='Сылка на профиль YouTube')
    social_link_linkedin = models.URLField(blank=True, null=True, verbose_name='Сылка на профиль LinkedIn')
    social_link_twitter = models.URLField(blank=True, null=True, verbose_name='Сылка на профиль Twitter')
    social_link_facebook = models.URLField(blank=True, null=True, verbose_name='Сылка на профиль FaceBook')
    social_link_other_1 = models.URLField(blank=True, null=True, verbose_name='Сылка на профиль 1')
    social_link_other_2 = models.URLField(blank=True, null=True, verbose_name='Сылка на профиль 2')


    def __str__(self):
        return self.site_name