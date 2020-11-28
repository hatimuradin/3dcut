from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'placeholder': 'نام'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'نام خانوادگی'}))
    email = forms.EmailField(max_length=150, widget=forms.TextInput(
        attrs={'placeholder': 'ایمیل'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'تکرار کلمه عبور'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )


class SignInForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'نام کاربری'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور'}))
