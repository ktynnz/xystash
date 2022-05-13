import email
from logging import PlaceHolder
from tabnanny import verbose
from django import forms

class contactForm(forms.Form):
    fullname = forms.CharField(max_length=100, label='Fullname')
    email = forms.CharField(max_length=100, label='Email', widget=forms.EmailInput)    
    message = forms.CharField(max_length=500, label='Message', widget=forms.Textarea(
        attrs={ 'class': 'msgbox'}))

class loginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Username', widget=forms.TextInput(attrs={'placeholder' : '@username'}))
    password = forms.CharField(max_length=100, label='New Password', widget=forms.PasswordInput(attrs={'placeholder' : 'password'}))

class signUpForm(forms.Form):
    firstName = forms.CharField(max_length=50, label='First Name', widget=forms.TextInput(attrs={'placeholder' : 'First Name'}))
    lastName = forms.CharField(max_length=50, label='Last Name', widget=forms.TextInput(attrs={'placeholder' : 'Last Name'}))
    email = forms.CharField(max_length=100, label='Email', widget=forms.EmailInput(attrs={ 'placeholder' : 'Email'}))
    # address = forms.CharField(max_length=100, label='Address')
    # city = forms.CharField(max_length=100, label='City')
    # province = forms.CharField(max_length=100, label='Province')
    # zipCode = forms.CharField(max_length=50, label='Zip Code')
    username = forms.CharField(max_length=100, label='Username', widget=forms.TextInput(attrs={'placeholder' : '@username'}))
    password = forms.CharField(max_length=100, label='New Password', widget=forms.PasswordInput(attrs={'placeholder' : 'password'}))

class subscribersForm(forms.Form):
    email = forms.CharField(max_length=50, label='Email', widget=forms.EmailInput(attrs={'placeholder' : 'your email here'}))
    