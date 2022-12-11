from django import forms
from django.core.validators import ValidationError
from django.contrib.auth.models import User

class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form_control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form_control'})
                           #    , validators=[
           # RegexValidator(
             #   '^(\w+\d+|\d+\w+){8,14}$',
            #    message="Password should be a combination of Alphabets and Numbers"
          #  )]
                               )
    #password = forms.RegexField('^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,14}$', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='confirm password',widget=forms.PasswordInput(attrs={'class': 'form_control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form_control'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('this email already exist')
        return email
    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('this username already exist')
        return username
    def clean(self):
        cleaned_data = super().clean()
        pass_main = cleaned_data.get('password')
        pass_confirm = cleaned_data.get('password_confirm')
        if pass_main and pass_confirm and pass_confirm != pass_main:
            raise ValidationError('password is not match')

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form_control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_control'}))


