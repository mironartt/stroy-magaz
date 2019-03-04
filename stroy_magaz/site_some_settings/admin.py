from django.contrib import admin
from .models import SiteSettings

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    """Модель настроек сайта"""

    list_display = ['site_name', 'confirm_main_comments', 'confirm_portfolio_comments',]
    save_on_top = True
    fieldsets = (
        (
            'Основные',
            {
                "fields": ("site_name", "avalible_load_files_order", "alert_email"),
            },
        ),
        (
            'Обработка коментариев',
            {
                "fields": ("confirm_main_comments", "confirm_portfolio_comments", "confirm_services_comments"),
            },
        ),
        (
            'Сылки на соцсети',
            {
                "fields": ("social_link_vk", "social_link_youtube", "social_link_linkedin",
                           "social_link_twitter", "social_link_facebook", "social_link_other_1",
                           "social_link_other_2",),
            },
        ),
        (
            'Оповещения',
            {
                "fields": ("alert_new_order", "alert_new_coll_back_order", "alert_new_main_comment",
                           "alert_new_portfolio_comments", "alert_new_services_comments",),
            },
        ),
        (
            'Шаблоны сообщений',
            {
                "fields": ("mail_subject_order_create", "mail_message_order_create", "mail_subject_comment_create", "mail_message_comment_create",
                           "mail_message_footer",),
            },
        ),
        (
            'Свои имена кнопок',
            {
                "fields": ("name_bottom_order", "name_bottom_coll_back",),
            },
        ),

        (
            'Статистика',
            {
                "fields": ("number_visits_day", "number_visits_month", "number_visits_all_time",),
            },
        ),
    )
