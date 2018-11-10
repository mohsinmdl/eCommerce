from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class ChangeUserPassword(PasswordChangeForm):

    def __init__(self,*args,**kwargs):
        super(ChangeUserPassword, self).__init__(*args,**kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = self.fields[field].label
            self.fields[field].label=''








class EditProfileForm(UserChangeForm):
        username = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': 'First Name',
                    'type': 'text'

                })
        )

        first_name = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': 'First Name',
                    'type': 'text'

                })
        )

        last_name = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': 'Last Name',
                    'type': 'text'

                })
        )

        email = forms.EmailField(
            widget=forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': 'Enter your email'
                }))

        password = forms.CharField(
            label='',
            widget=forms.TextInput(attrs={'type': 'hidden'})
        )

        class Meta:
            model = User
            fields = ('username', 'first_name', 'last_name', 'email', 'password')

class SignUpForm(UserCreationForm):
        first_name = forms.CharField(
            label='',
            widget=forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': 'First Name',
                    'type': 'text'

                })
        )

        last_name = forms.CharField(
            label='',
            widget=forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': 'Last Name',
                    'type': 'text'

                })
        )
        email = forms.EmailField(
            label='',
            widget=forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': 'Enter your email'
                }))

        class Meta:
            model = User
            fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

        def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, *kwargs)

            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['Placeholder'] = 'Username'
            self.fields['username'].label = ''

            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['Placeholder'] = 'Password'
            self.fields['password1'].label = ''

            self.fields['password2'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['Placeholder'] = 'Password confirmation'
            self.fields['password2'].label = ''
