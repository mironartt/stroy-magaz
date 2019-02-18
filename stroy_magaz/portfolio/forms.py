from django import forms
from .models.comments import PortfolioComments

class PortfolioCommentsForm(forms.ModelForm):
    name_person = forms.CharField(label='* ФИО / Название компании', error_messages={
        'required': 'Данное поле обязательно к заполнение. Пожалуйста введите данные корректно.',
        'invalid': 'Введите данные корректно!'},
                                  required=True, widget=forms.TextInput(
            attrs={'placeholder': '** Ваше полное имя / Название компании'}))

    email = forms.EmailField(label='* Ваш Email', error_messages={'invalid': 'Введите email корректно!',
                                                                         'required': 'Это поле обязательно. '}, )

    comment_body = forms.CharField(label='* Коментарий',
                                         error_messages={'required': 'Это поле обязательно. ', 'invalid': 'Введите данные корректно!'},
                                         required=True,
                                         widget=forms.Textarea(
                                             attrs={'type': 'text',
                                                    'placeholder': '** Ваш коментарий'}))


    class Meta(object):
        model = PortfolioComments
        fields = ['name_person', 'email', 'comment_body', 'parent_object']




