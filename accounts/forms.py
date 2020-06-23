from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=255,required=True,label='Email')
    password = forms.CharField(max_length=255,widget=forms.PasswordInput,required=True,label='Password')

    def clean(self):
        usern = self.cleaned_data.get('email')
        passw = self.cleaned_data.get('password')
        user = authenticate(username=usern,password=passw)
        user2 = authenticate(email=usern,password=passw)

        if not user and not user2:
            raise forms.ValidationError('user does not exists!')




class RegisterForm(forms.Form):
    email = forms.EmailField(max_length=255,required=True,label='Email')
    password = forms.CharField(max_length=20,widget=forms.PasswordInput,required=True,label='Password',min_length=8)

    def clean(self):
        username = self.cleaned_data.get('email')
        user = User.objects.filter(username=username)
        user2 = User.objects.filter(email=username)
        if user.exists() or user2.exists():
            raise forms.ValidationError('Email has registered!')
