from re import M
from django import forms
from django.forms import NumberInput, ModelForm, TextInput, Textarea, Select, PasswordInput, DateInput, SelectMultiple, MultipleChoiceField
from django.contrib.auth.models import User
from ViewMovie.models import Movie, Review, UserInfo


class UserInfoForm(forms.ModelForm):

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'password')
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'auto-complete': 'off',


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


class AddMovieForm(ModelForm):

    class Meta():

        model = Movie
        fields = ('title', 'released', 'rated', 'plot', 'genre', 'actors',
                  'directors', 'runtime', 'collection', 'writers', 'poster', 'awards')

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',

            }),
            'released': DateInput(attrs={
                'class': 'form-control',

                'type': 'date'
            }),
            'rated': Select(attrs={
                'class': 'form-select',

            }),
            'genre': SelectMultiple(attrs={
                'class': 'form-select'
            }),
            'collection': TextInput(attrs={
                'class': 'form-control'
            }),

            'runtime': TextInput(attrs={
                'class': 'form-control',

            }),
            'plot': Textarea(attrs={
                'class': 'form-control',
                'style': 'height:92px',
                'rows': 5,
                'cols': 100,
            }),

            'actors': TextInput(attrs={
                'class': 'form-control',

            }),
            'directors': TextInput(attrs={
                'class': 'form-control',

            }),
            'writers': TextInput(attrs={
                'class': 'form-control',

            }),
            'awards': TextInput(attrs={
                'class': 'form-control',

            }),
            'poster': TextInput(attrs={
                'class': 'form-control',

            }),

        }


class ReviewForm(ModelForm):

    class Meta():
        model = Review
        fields = ('review_score',
                  'review_summary', 'full_review')

        widgets = {
            'review_score': NumberInput(attrs={
                'class': 'form-control',
                'style': 'margin-top:10px',
                'min': 0,
                'max': 10,
            }),
            'review_summary': TextInput(attrs={
                'class': 'form-control',
                'style': 'margin-top:10px'
            }),
            'full_review': Textarea(attrs={
                'class': 'form-control',
                'style': 'height:100px; margin-top:10px;',
                'rows': 5,
                'cols': 100
            })
        }
