from django import forms
from .models import Table
from django.forms import TextInput, NumberInput



class UserForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['name', 'last_name', 'money', 'month']
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
            'month': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите месяц'
            })
        }






