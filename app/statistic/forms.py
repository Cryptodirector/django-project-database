from django import forms
from .models import Table
from django.forms import TextInput, NumberInput



class UserForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['name', 'last_name', 'money', 'service', 'month']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }),
            'money': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите стоимость услуги'
            }),

            'service': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите услугу'
            }),

            'month': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите месяц'
            })
        }






