from django import forms 


class RegistrationForm(forms.Form):
    username=forms.CharField()
    first_name=forms.CharField()
    last_name=forms.CharField()
    email=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

