from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.Form):
    username=forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'class':'form_control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form_control'}))
    password1=forms.CharField(label='password' , widget=forms.PasswordInput(attrs={'class':'form_control'}))
    password2=forms.CharField(label='confirm password' , widget=forms.PasswordInput(attrs={'class':'form_control'}))
    
    def clean_email(self):
        email=self.cleaned_data['email']
        user=User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('this email address already exists')
        return email
    
    def clean(self):
        cd= super().clean()
        p1=cd.get['password1']
        p2=cd.get['password2']
        if p1 and p2 and p1!=p2:
            raise ValidationError('passwords didn`t match')
        
 