from django import forms
from .models.main_comments import MainComments
from service.models.kindworks import KindWorks
from .models.coll_back import CollBackClient
from .models.order import Order

from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


if KindWorks.objects.all():
    KIND_WORKS = [
        (i, str(i)) for i in KindWorks.objects.all()
        ]
else:
    KIND_WORKS = [
        ('Разное','Разное')
        ]

KIND_WORKED = [
        ('Другое','Другое')
        ]

KIND_WORKS +=KIND_WORKED

# your_list = [[[] for x in range(9)] for y in range(10)]


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in reversed(range(1, 11))]

class MainCommentsForm(forms.ModelForm):
    # job_satisfaction = forms.CharField( max_length=64, widget=forms.Select(choices=PRODUCT_QUANTITY_CHOICES, ))
    name_person = forms.CharField(label='* ФИО / Название компании', error_messages={'required': 'Данное поле обязательно к заполнение. Пожалуйста введите данные корректно.'}, widget=forms.TextInput(attrs={'placeholder':'** Ваше полное имя / Название компании'}))
    email = forms.EmailField(label='* Ваш Email', error_messages={'invalid': 'Введите email корректно!', 'required':'Это поле обязательно. '},)

    phone = forms.CharField(label='Телефон', error_messages={'invalid': 'Введите телефон корректно!'}, required=False,
        widget=forms.TextInput(attrs={'class': 'required', 'type': 'number', 'placeholder': 'Ваш телефон'}))

    comment_body = forms.CharField(label='Ваш отзыв', error_messages={'invalid': 'Введите данные корректно!'}, required=False,
        widget=forms.Textarea(attrs={'class': 'required', 'type': 'text', 'placeholder': 'Ваш отзыв'}))

    job_satisfaction = forms.CharField(label='** Ваша оценка произведенным работам',
        widget=forms.Select(choices=PRODUCT_QUANTITY_CHOICES, attrs={'class': 'select select--left',}))

    kind_job = forms.CharField(label='** Какие работы у вас производились',
                                       widget=forms.Select(choices=KIND_WORKS,attrs={'class': 'select select--left',}))

    class Meta:
        model = MainComments
        fields = ['name_person', 'email', 'phone', 'kind_job', 'job_satisfaction', 'comment_body', ]
        # widgets = {
        #     'job_satisfaction': forms.Select(attrs={'class': 'selectpicker input-price', 'data-width': '100%', }),
        #     # 'payment_methon': forms.Select(attrs={'class': 'selectpicker input-price', 'data-width': '100%', }),
        # }






class CollBackClientForm(forms.ModelForm):
    name_client = forms.CharField(label='* ФИО / Название компании', error_messages={
        'required': 'Данное поле обязательно к заполнение. Пожалуйста введите данные корректно.', 'invalid': 'Введите данные корректно!'},
                                  required=True, widget=forms.TextInput(
                                      attrs={'placeholder': '** Ваше полное имя / Название компании'}))
    phone_client = forms.CharField(label='Телефон', error_messages={'invalid': 'Введите телефон корректно!', 'required': 'Данное поле обязательно к заполнение!'},
                            required=True, widget=forms.TextInput(
                                attrs={'class': 'required', 'type': 'number', 'placeholder': 'Ваш телефон'}))

    coll_time = forms.CharField(label='* Время когда перезвонить', error_messages={
        'required': 'Данное поле обязательно к заполнение. Пожалуйста введите данные корректно.', 'invalid': 'Введите данные корректно!'},
                                  required=True, widget=forms.TextInput(
                                      attrs={'placeholder': '** Кода перезвонить'}))

    description_client = forms.CharField(label='Примечания', error_messages={'invalid': 'Введите данные корректно!'},
                                   required=False,
                                   widget=forms.Textarea(
                                       attrs={'class': 'required', 'type': 'text', 'placeholder': 'Предварительное описание, для того чтобы мы подготовились к тому что вам необходимо'}))

    class Meta:
        model = CollBackClient
        fields = ['name_client', 'phone_client', 'coll_time', 'description_client', ]








class OrderCreateForm(forms.ModelForm):
    name_client = forms.CharField(label='* ФИО / Название компании', error_messages={
        'required': 'Данное поле обязательно к заполнение. Пожалуйста введите данные корректно.',
        'invalid': 'Введите данные корректно!'},
                                  required=True, widget=forms.TextInput(
                                      attrs={'placeholder': '** Ваше полное имя / Название компании'}))
    phone_client = forms.CharField(label='Телефон', error_messages={'invalid':'Введите телефон корректно!', 'required':'Данное поле обязательно к заполнение!'},
                            required=True, widget=forms.TextInput(
                                attrs={'class': 'required', 'type': 'number', 'placeholder': 'Ваш телефон'}))


    email_client = forms.EmailField(label='* Ваш Email', error_messages={'invalid': 'Введите email корректно!',
                                                                  'required': 'Это поле обязательно. '}, )

    description_client = forms.CharField(label='Описание заказа', error_messages={'invalid': 'Введите данные корректно!'},
                                         required=False,
                                         widget=forms.Textarea(
                                             attrs={'type': 'text',
                                                    'placeholder': 'Описание заказа'}))

    subject_work = forms.CharField(label='* Тематика работ', error_messages={'invalid': 'Введите данные корректно!'},
                                         required=True,
                                         widget=forms.TextInput(
                                             attrs={'type': 'text',
                                                    'placeholder': '** Тематика работ'}))


    file = forms.FileField(required=False, label='Файлы', help_text='Совет: если необходимо загрузить несколько файлов, добавьте их все в архив и загрузите его')



    #
    # MAX_UPLOAD_SIZE = "2621440"
    #
    # # Add to a form containing a FileField and change the field names accordingly.
    #
    # def clean_file(self):
    #     content = self.cleaned_data['file']
    #     content_type = content.content_type.split('/')[0]
    #     if content_type in settings.CONTENT_TYPES:
    #         if content._size > settings.MAX_UPLOAD_SIZE:
    #             raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (
    #             filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(content._size)))
    #     else:
    #         raise forms.ValidationError(_('File type is not supported'))
    #     return content

    class Meta:
        model = Order
        fields = ['name_client', 'phone_client', 'email_client', 'subject_work', 'description_client', 'file']
    #
    # def clean_file(self):
    #     CONTENT_TYPES = ['image']
    #     MAX_UPLOAD_PHOTO_SIZE = "2621440"
    #     content = self.cleaned_data['file']
    #     content_type = content.content_type.split('/')[0]
    #     if content_type in CONTENT_TYPES:
    #         if content._size > MAX_UPLOAD_PHOTO_SIZE:
    #             msg = 'Keep your file size under %s. actual size %s' \
    #                   % (filesizeformat(settings.MAX_UPLOAD_PHOTO_SIZE), filesizeformat(content._size))
    #             raise forms.ValidationError(msg)
    #
    #         if not content.name.endswith('.jpg'):
    #             msg = 'Your file is not jpg'
    #             raise forms.ValidationError(msg)
    #     else:
    #         raise forms.ValidationError('File not supported')
    #     return content

    CONTENT_TYPES = ['image', 'video', 'archive',]
    # 2.5MB - 2621440
    # 5MB - 5242880
    # 10MB - 10485760
    # 20MB - 20971520
    # 50MB - 5242880
    # 100MB 104857600
    # 250MB - 214958080
    # 500MB - 429916160
    MAX_UPLOAD_SIZE = "2621440"

    # Add to a form containing a FileField and change the field names accordingly.
    # from django.template.defaultfilters import filesizeformat
    # from django.utils.translation import ugettext_lazy as _
    # from django.conf import settings
    def clean_content(self):
        content = self.cleaned_data['file']
        content_type = content.content_type.split('/')[0]
        if content_type in settings.CONTENT_TYPES:
            if content._size > settings.MAX_UPLOAD_SIZE:
                raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (
                filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(content._size)))
        else:
            raise forms.ValidationError(_('File type is not supported'))
        return content



#
#
#
# class OrderCreateForm(forms.ModelForm):
#     full_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'text', 'placeholder':'** Ваше полное имя'}))
#     email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': '** Ваш email'}))
#     phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '** Ваш телефон'}))
#     street = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '** Улица'}))
#     house = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '** № дома'}))
#     building = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Строение/Корпус'}))
#     entrance = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '№ подъезда'}))
#     doorphone = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Код домофона'}))
#     floor = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '№ этажа'}))
#     apartment = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': '№ квартиры'}))
#     notes = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'cols': '30', 'rows': '10', 'placeholder': 'Примечания к заказу'}))
#
#
#
#
#
#     class Meta:
#         model = Order
#         fields = ['full_name', 'email', 'phone', 'street', 'house', 'delivery_method',
#                   'payment_methon', 'building', 'entrance', 'doorphone', 'floor', 'apartment', 'notes']
#
#         widgets = {
#             'delivery_method': forms.Select(attrs={'class':'selectpicker input-price', 'data-width':'100%',}),
#             'payment_methon': forms.Select(attrs={'class': 'selectpicker input-price', 'data-width': '100%', }),
#         }
#
#
# class DeliveryPayment(forms.ModelForm):
#
#     # delivery_method = forms.Select(widget=forms.Select(attrs={'class':'selectpicker input-price', 'data-live-search':'true', 'data-width':'100%', 'data-toggle':'tooltip', 'title':'Select'}))
#
#
#     class Meta:
#         model = Order
#         fields = ['delivery_method', 'payment_methon']
#
#         widgets = {
#             'delivery_method': forms.Select(attrs={'class':'selectpicker input-price', 'data-width':'100%', 'data-toggle':'tooltip', 'title':'1', 'data-live-search':'true'}),
#         }
#
#
#
#
