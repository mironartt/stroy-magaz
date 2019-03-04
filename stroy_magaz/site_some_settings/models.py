from django.db import models



class SiteSettings(models.Model):
    """
        Модель управление некоторыми настройками сайта
        Только одна модель
    """

    class Meta:
        verbose_name = 'Настройки сайта (только одна модель)'
        verbose_name_plural = 'Настройки сайта (только одна модель)'


    site_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Название сайта отображается в название вкладки')
    confirm_main_comments = models.BooleanField(default=False,
                                                     verbose_name="""Публикация отзывов в разделе "отзывы" без модерации""")
    confirm_portfolio_comments = models.BooleanField(default=False, verbose_name='Публикация коментариев в разделе портфолио без модерации')

    confirm_services_comments = models.BooleanField(default=False,
                                                     verbose_name='Публикация коментариев в разделе "типы работ и усуи" без модерации')

    avalible_load_files_order = models.BooleanField(default=True,
                                                     verbose_name='Разрешить клиентам загружать файлы на сервер')


    alert_email = models.EmailField(blank=True, null=True, verbose_name='Email на которые будут приходить оповещения')
    alert_new_order = models.BooleanField(default=True, verbose_name='Оповещать о новом заказе')
    alert_new_coll_back_order = models.BooleanField(default=True, verbose_name='Оповещать о новой заявке на обратный звонок')
    alert_new_main_comment = models.BooleanField(default=True, verbose_name='Оповещать о новых отзывах')
    alert_new_portfolio_comments = models.BooleanField(default=True, verbose_name='Оповещать о новых коментариях в разделе "портфолио"')
    alert_new_services_comments = models.BooleanField(default=True, verbose_name='Оповещать о новых коментариях в разделе "предоставляемые услуги"')


    mail_subject_order_create = models.CharField(max_length=200, blank=True, null=True, verbose_name='Текст темы сообщения оправляемого клиенту при успешном оформлении им заказа')
    mail_subject_comment_create = models.CharField(max_length=200, blank=True, null=True,
                                                 verbose_name='Текст темы сообщения оправляемого клиенту при успешном добавлении какого либо коментария или отзыва')

    mail_message_order_create = models.TextField(blank=True, null=True,
                                                 verbose_name='Текст сообщения оправляемого клиенту при успешном оформлении им заказа')
    mail_message_comment_create = models.TextField(blank=True, null=True,
                                                 verbose_name='Текст сообщения оправляемого клиенту при успешном добавление коментария')

    mail_message_footer = models.TextField(blank=True, null=True,
                                                 verbose_name='Текст в низу сообщения (пожелания, с уважением)')

    name_bottom_order = models.CharField(max_length=100, blank=True, null=True, verbose_name='Текст на кнопке оформления заказа')
    name_bottom_coll_back = models.CharField(max_length=100, blank=True, null=True,
                                         verbose_name='Текст на кнопке оформления заказа на обратный звонок')



    social_link_vk = models.URLField(blank=True, null=True, verbose_name='Сылка на профиль ВК')
    social_link_youtube = models.URLField(blank=True, null=True, verbose_name='Сылка на профиль YouTube')
    social_link_linkedin = models.URLField(blank=True, null=True, verbose_name='Сылка на профиль LinkedIn')
    social_link_twitter = models.URLField(blank=True, null=True, verbose_name='Сылка на профиль Twitter')
    social_link_facebook = models.URLField(blank=True, null=True, verbose_name='Сылка на профиль FaceBook')
    social_link_other_1 = models.URLField(blank=True, null=True, verbose_name='Сылка на профиль 1')
    social_link_other_2 = models.URLField(blank=True, null=True, verbose_name='Сылка на профиль 2')

    last_day = models.DateTimeField(blank=True, null=True, verbose_name='День от которого идет счет 24 часов',)
    last_month = models.DateTimeField(blank=True, null=True, verbose_name='Месяц от которого идет счет')
    number_visits_day = models.IntegerField(blank=True, null=True, verbose_name='Число посещений за день')
    number_visits_month = models.IntegerField(blank=True, null=True, verbose_name='Число посещений за месяц')
    number_visits_all_time = models.IntegerField(blank=True, null=True, verbose_name='Число посещений за все время')

    # def __init__(self):
    #     if not self.number_visits_day:
    #         self.number_visits_day = 0


    def __str__(self):
        return self.site_name


