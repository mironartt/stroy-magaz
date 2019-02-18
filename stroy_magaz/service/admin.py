from django.contrib import admin
from .models.images import Images
from .models.kindworks import KindWorks
from .models.service import Service, Unit
from .models.comments import KindWorksComments, ServiceComments

from import_export import resources
from import_export.admin import ImportExportModelAdmin



@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    """
    Модель изображений относящихся к галлереи
    """
    list_display = ['name', 'image_img', 'image', 'description', 'slug', 'created', 'updated']
    readonly_fields = ['image_img', ]
    search_fields = ('descriptions', )
    prepopulated_fields = {'slug': ('name',)}








class KindWorksResource(resources.ModelResource):
    class Meta:
        model = KindWorks
        export_order = ('id', 'name', 'slug', 'intro', 'main_image', 'image', 'created', 'updated', 'gallery_availability')
        """ImportExportModelAdmin"""
@admin.register(KindWorks)
class KindWorksAdmin(ImportExportModelAdmin):
    """
    Модель возможных типов работ
    """
    list_display = ['name', 'image_img', 'obj_id', 'slug', 'created', 'updated',]
    readonly_fields = ['image_img', 'obj_id']
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}







class ServiceResource(resources.ModelResource):
    class Meta:
        model = Service
        export_order = ('id', 'kindworks', 'name', 'slug', 'image', 'main_image', 'desctiptions', 'created', 'updated', 'price', 'unit', 'gallery_availability')
        """ImportExportModelAdmin"""
@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin):
    """
    Модель предоставляемый услуг работы
    """
    list_display = ['name', 'image_img', 'kindworks', 'slug', 'price', 'unit', 'created', 'updated',]
    readonly_fields = ['image_img', ]
    list_filter = ['kindworks']
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    """
    Модель единиц измерения
    """
    list_display = ['name', ]






class KindWorksCommentsResource(resources.ModelResource):
    class Meta:
        model = KindWorksComments
        export_order = ('id', 'parent_object', 'name_person', 'email', 'comment_body','created', 'updated', 'moderation')
        """ImportExportModelAdmin"""
@admin.register(KindWorksComments)
class KindWorksCommentsCommentsAdmin(ImportExportModelAdmin):
    """
    Модель Коментариев для объектов "типы работ"
    """
    list_display = ['name_person','obj_name', 'moderation', 'email', 'comment_body', 'created', 'updated',]
    list_editable = ['moderation']
    readonly_fields = ['obj_name', ]
    list_filter = ['moderation',]
    search_fields = ('name_person', 'email', 'comment_body',)




class ServiceCommentsResource(resources.ModelResource):
    class Meta:
        model = ServiceComments
        export_order = ('id', 'parent_object', 'name_person', 'email', 'comment_body','created', 'updated', 'moderation')
        """ImportExportModelAdmin"""
@admin.register(ServiceComments)
class ServiceCommentsAdmin(ImportExportModelAdmin):
    """
    Модель Коментариев для объектов "предоставляемые услуги"
    """
    list_display = ['name_person','obj_name', 'moderation', 'email', 'comment_body', 'created', 'updated',]
    list_editable = ['moderation']
    readonly_fields = ['obj_name', ]
    list_filter = ['moderation',]
    search_fields = ('name_person', 'email', 'comment_body',)