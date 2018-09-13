from django import forms
from django.contrib.auth import get_user_model

Users = get_user_model()
class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': 'Enter your full name'
            }))

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': 'Enter your email'
            }))

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': "form-control",
                'placeholder': 'Enter your Message'
            }))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Please enter gmail domain only")
        return email


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Password'
    }))


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': 'Enter your email'
            }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Password'
    }))

    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Password'
    }))

    def clean_username(self):
        data = self.cleaned_data
        username = self.cleaned_data.get("username")
        qs = Users.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is already exist")
        return username

    def clean_email(self):
        data = self.cleaned_data
        email = self.cleaned_data.get("email")
        qs = Users.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is already exist")
        return email


    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("Password must match.")
        return data
