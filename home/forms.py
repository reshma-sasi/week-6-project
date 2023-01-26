from django import forms 
from .models import Amodel
from django.contrib.auth.models import User
import re

 
class student(forms.ModelForm):
     class Meta:
         model=Amodel
         fields = ['name','email','password']
         widgets={
             'name':forms.TextInput(attrs={'class': 'form-control'}),
             'email':forms.EmailInput(attrs={'class': 'form-control'}),
             'password':forms.PasswordInput(attrs={'class': 'form-control'}), 
         }
         
     def clean(self):
            username = self.cleaned_data['name']
            password = self.cleaned_data['password']
            email = self.cleaned_data['email']

            if not re.match("^[A-Za-z]{3,12}$",username):
                raise forms.ValidationError("username only alow alphabets ")

            if len(password) < 4 or len(password)> 12:
                raise forms.ValidationError("password length beetween 4 - 12 ")
            
            if not (re.match("^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$",email)):
                raise forms.ValidationError("Email id is not valid")
            


         
         
class admin(forms.ModelForm):
     class Meta:
         model=User
         fields = ['username','email','password']
         widgets={
             'username':forms.TextInput(attrs={'class': 'form-control'}),
             'email':forms.EmailInput(attrs={'class': 'form-control'}),
             'password':forms.TextInput(attrs={'class': 'form-control'}), 
         }