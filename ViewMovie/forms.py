from django import forms
from django.contrib.auth.models import User
from ViewMovie.models import UserInfo


class UserInfoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'password')
