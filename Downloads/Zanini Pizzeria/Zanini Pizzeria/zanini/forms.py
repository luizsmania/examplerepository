from django import forms
from django.forms import EmailInput, TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Reservation
from django.shortcuts import render
from datetime import date


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table_size', 'booking_time', 'date']
        widgets = {
            'date': forms.DateInput(attrs={
                'class': 'datepicker form-control form-floating mb-3',
                'placeholder': 'Select a date',
                'value': date.today().strftime('%Y-%m-%d'),  # Set the default value to today's date
            }),
            'table_size': forms.Select(attrs={
                'class': 'form-control form-floating mb-3',
                'placeholder': 'Select table size',
            }),
            'booking_time': forms.Select(attrs={
                'class': 'form-control form-floating mb-3',
                'placeholder': 'Select booking time',
            }),
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65, widget=forms.TextInput(
        attrs={'placeholder': 'Username',
               'style': 'width: 300px;',
               'class': 'form-control'}))
    password = forms.CharField(max_length=65, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password',
               'style': 'width: 300px;',
               'class': 'form-control'}))


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
           
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder':'password', 'style': 'max-width: 300px;'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder':'password', 'style': 'max-width: 300px;',}),
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Username'
                }),
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'First Name'
                }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),
        }
