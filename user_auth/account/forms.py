from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label='password2',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["username","email"]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    
    def clean_email(self):
        cd = self.cleaned_data
        if User.objects.filter(email = cd['email']).exists():
            raise forms.ValidationError('User with this email already exists')
        return cd['email']