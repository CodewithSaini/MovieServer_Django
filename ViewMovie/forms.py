from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django.contrib.auth.models import User
from ViewMovie.models import UserInfo


class UserInfoForm(forms.ModelForm):

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'password')
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'auto-complete': 'off'

            }),
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name',

            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name',

            }),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'auto-complete': 'off'


            })
        }


class UserLogInForm(ModelForm):
    password = forms.CharField(widget=PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password')
