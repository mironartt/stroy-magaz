from django.contrib import admin
from .models.images import Images
from .models.portfolio import Portfolio, Topic
from .models.comments import PortfolioComments
from import_export import resources
from import_export.admin import ImportExportModelAdmin



class PortfolioCommentsResource(resources.ModelResource):
    class Meta:
        model = PortfolioComments
        export_order = ('id', 'parent_object', 'name_person', 'email', 'comment_body', 'created', 'updated', 'moderation')

@admin.register(PortfolioComments)
class PortfolioCommentsAdmin(ImportExportModelAdmin):
    """Модель Коментариев для объектов портфолио"""

    save_on_top = True
    list_display = ['name_person','obj_name', 'moderation', 'email', 'comment_body', 'watched', 'created', 'updated',]
    list_editable = ['moderation']
    readonly_fields = ['obj_name', ]
    list_filter = ['moderation', 'watched']
    search_fields = ('name_person', 'email', 'comment_body',)






@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    """Модель общей галлереи для раздела портфолио"""

    save_on_top = True
    list_display = ['name', 'image_img', 'image', 'description', 'slug', 'created', 'updated']
    readonly_fields = ['image_img', ]
    search_fields = ('descriptions', )
    prepopulated_fields = {'slug': ('name',)}





class PortfolioResource(resources.ModelResource):
    class Meta:
        model = Portfolio
        export_order = ('id', 'topic', 'name', 'slug', 'description', 'main_image', 'images', 'created', 'updated', 'availability')

@admin.register(Portfolio)
class PortfolioAdmin(ImportExportModelAdmin):
    """Модель портфолио"""

    save_on_top = True
    list_display = ['name', 'obj_id', 'image_img', 'topic', 'availability', 'slug',  'created', 'updated',]
    readonly_fields = ['image_img', 'obj_id',]
    list_filter = ['topic']
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    """Модель категорий для раздела портфолио"""

    save_on_top = True
    list_display = ['name', 'descriprion', 'slug', ]
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}



