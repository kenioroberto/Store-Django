from dataclasses import fields
from socket import fromshare
from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password =  forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Digite senha',
        'class': 'form-control',
    }))
    confirm_password =  forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirmar senha',
        'class': 'form-control',
    }))

       
    
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    

    def clean(self):
        clean_data = super(RegistrationForm, self).clean()
        password = clean_data.get('password')
        confirm_password = clean_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Senhas não comferem!"
            )
        
    def __init__(self,*args, **kwargs):
        super(RegistrationForm, self).__init__(*args, *kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Primeiro nome'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Segundo nome'
        self.fields['email'].widget.attrs['placeholder'] = 'Digite seu e-mail'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Digite seu telefone com DDD'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'