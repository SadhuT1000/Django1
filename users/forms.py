from phonenumber_field.formfields import PhoneNumberField
from django.forms import ModelForm, BooleanField
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django import forms
from catalog.froms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class ClientForm(UserCreationForm):
    phone = PhoneNumberField()
