from django import forms
from django_registration.forms import RegistrationForm
from django.contrib.auth import authenticate
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from .models import User


class CustomUserCreationForm(RegistrationForm):
    phone_number=PhoneNumberField(widget=PhoneNumberPrefixWidget)
    class Meta(RegistrationForm.Meta):
        model=User
        fields=('username','email','first_name','last_name','phone_number','password1','password2')

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')

        if username and password:
            try:
                user=authenticate(username=User.objects.get(email=username),password=password)
            except:
                user=authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError('The user does not exist')
        return super(LoginForm,self).clean(*args,**kwargs)