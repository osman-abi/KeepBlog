from django import forms
from django.forms import widgets
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=200,
        label='First Name',
        error_messages={
            'required': 'This field is required',
            'max_length': 'Entered characters is too long'
        }
    )
    last_name = forms.CharField(
        max_length=200,
        label='Last Name',
        error_messages={
            'required': 'This field is required',
            'max_length': 'Entered characters is too long'
        }
    )
    email = forms.EmailField(
        max_length=200,
        label='Email',
        error_messages={
            'required': 'This field is required',
            'invalid': 'You have to assign @ property to your email information'
        }
    )
    password = forms.CharField(
        max_length=200,
        label='Password',
        error_messages={
            'required': 'This field is required',
        }
    )


    class Meta:
        model = User
        fields = ('first_name','last_name','email','password')

    def __init__(self,*args,**kwargs):
        super(RegisterForm, self).__init__(*args,**kwargs)

        self.fields.get('first_name').widget.attrs.update({
            'class': 'form-control border-success',
            'type': 'text',
            'max': '200'
        })
        self.fields.get('last_name').widget.attrs.update({
            'class': 'form-control border-success',
            'type': 'text',
            'max': '200'
        })
        self.fields.get('email').widget.attrs.update({
            'class': 'form-control border-success',
            'type': 'email',
            'max': '200'
        })
        self.fields.get('password').widget = widgets.PasswordInput(
            attrs={
                'class': 'form-control border-success',
                'type': 'password',
                'name': 'password',
                'max': '200'
            }
        )


class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        max_length=200,
        label='Email',
        error_messages={
            'required': 'This field is required'
        }
    )
    password = forms.CharField(
        max_length=200,
        label='Password',
        error_messages={
            'required': 'This field is required'
        }
    )

    class Meta:
        model = User
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields.get('username').widget = widgets.EmailInput(
            attrs={
                'class': 'form-control border-success',
                'type': 'email',
                'name': 'email',
                'max': '200'
            }
        )
        self.fields.get('password').widget = widgets.PasswordInput(
            attrs={
                'class': 'form-control border-success',
                'type': 'password',
                'name':'password',
                'max': '200'
            }
        )

