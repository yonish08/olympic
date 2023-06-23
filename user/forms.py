from django import forms
from core.models import (
    Customer,
)
from django.contrib.auth.forms import UserCreationForm

# user authentication form
class UsersAuthenticationForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': "Enter email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Enter password"}))


# register form
class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=200,
        help_text='Required',
        widget=forms.EmailInput(attrs={'autocomplete': False,'placeholder': 'Enter your email'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'})
        )
    password2 = forms.CharField(
        label='Confirm password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'})
        )

    class Meta:
        model = Customer
        fields = ['full_name', 'email', 'country', 'password1', 'password2']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'country': forms.Select(attrs={'placeholder': 'Select country'}),
        }
