from django import forms
from .models.main_comments import MainComments
from service.models.kindworks import KindWorks
from .models.coll_back import CollBackClient
from .models.order import Order


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

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in reversed(range(1, 11))]

class MainCommentsForm(forms.ModelForm):
    """Форма добавления отзывов на сайт"""

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




class CollBackClientForm(forms.ModelForm):
    """Форма создания заказа обратного звонка"""

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
    """Форма создания Заказа"""

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


    class Meta:
        model = Order
        fields = ['name_client', 'phone_client', 'email_client', 'subject_work', 'description_client', 'file']
