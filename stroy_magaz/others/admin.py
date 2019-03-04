from django.contrib import admin
from .models.faq import Faq
from .models.home import HomePageText
from .models.main_slider import MainSlider
from .models.about_us import AboutUs
from .models.partners import Partners
from .models.main_comments import MainComments
from .models.coll_back import CollBack, CollBackClient
from .models.order import Order
from .models.documentation import Documentation
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class MainCommentsResource(resources.ModelResource):
    class Meta:
        model = MainComments
        export_order = ('id', 'name_person', 'email', 'phone', 'job_satisfaction', 'kind_job', 'comment_body', 'created', 'updated', 'moderation')
@admin.register(MainComments)
class MainCommentsAdmin(ImportExportModelAdmin):
    """Отзывы клиентов"""
    save_on_top = True
    list_display = ['name_person', 'moderation', 'email', 'kind_job', 'phone', 'job_satisfaction', 'created', 'updated',]
    list_editable = ['moderation']
    list_filter = ['job_satisfaction', 'moderation', 'kind_job']
    search_fields = ('name_person', 'phone', 'email', 'comment_body',)



class OrderResource(resources.ModelResource):
    class Meta:
        model = Order
        export_order = ('id', 'name_client', 'phone_client', 'email_client', 'subject_work', 'description_client', 'file', 'created', 'updated')
@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    """Заказ оставленный клиентом"""
    save_on_top = True
    list_display = ['name_client', 'watched', 'phone_client', 'email_client', 'subject_work', 'created', 'updated']
    search_fields = ('name_client', 'phone_client', 'email_client', 'subject_work',)
    list_filter = ['watched', ]


class CollBackClientResource(resources.ModelResource):
    class Meta:
        model = CollBackClient
        export_order = ('id', 'name_client', 'phone_client', 'coll_time', 'description_client', 'created', 'updated')
@admin.register(CollBackClient)
class CollBackClientAdmin(ImportExportModelAdmin):
    """Заказ клиента чтобы перезвонили"""
    save_on_top = True
    list_display = ['name_client', 'phone_client', 'coll_time', 'watched', 'description_client', 'created', 'updated']
    search_fields = ('name_client', 'phone_client', 'coll_time''watched',  'description_client',)
    list_filter = ['watched', ]




@admin.register(HomePageText)
class HomePageTextAdmin(admin.ModelAdmin):
    """Текст на главной странице"""
    save_on_top = True
    list_display = ['text_home_page', 'text_home_page_2']


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    """Раздел партнеры"""
    save_on_top = True
    list_display = ['name', 'image_img',]
    readonly_fields = ['image_img', ]
    list_display_links = ('image_img', 'name', )

@admin.register(MainSlider)
class MainSliderAdmin(admin.ModelAdmin):
    """Слайдер на главной странице"""
    save_on_top = True
    list_display = ['serial_number', 'image_img', 'title', 'description', 'button_name']
    readonly_fields = ['image_img', ]
    list_display_links = ('image_img', 'title', 'serial_number')

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    """Раздел FAQ"""
    save_on_top = True
    list_display = ['question', 'answer']


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    """Раздел "о нас" """
    save_on_top = True
    list_display = ['smal_company_name', 'phone', 'address','time_work', 'email']
    fieldsets = (
        (
            'Основные настройки',
            {
                "fields": ("smal_company_name", "discription_name", "email", "phone", "address", "time_work", "title_notes", "notes",),
                # "classes": (("collapse",),),
            },
        ),
        (
            'Тексты на страницах "Контакты" и "О компании"',
            {
                "fields": ("text_about_us_page", "text_about_us_page_2",),
            },
        ),
        (
            'Реквизиты в разеделе "Контакты"',
            {
                "fields": ("full_company_name", "fio_entrepreneur", "ip_registration_address", "inn_kpp", "bin",
                           "okved", "okpo", "requisites", "self_phone", "self_email",),
                # "classes": (("collapse",),),
            },
        ),
    )





@admin.register(CollBack)
class CollBackAdmin(admin.ModelAdmin):
    """Форма для главной страницы"""
    save_on_top = True
    list_display = ['title', 'avalible', 'description_short', 'btn_name', 'image_img',]
    readonly_fields = ['image_img', ]


@admin.register(Documentation)
class DocumentationAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['title', 'description', 'file', 'created', 'updated']
    search_fields = ('title', 'description', 'file', 'created', 'updated')



