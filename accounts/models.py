from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'phone_number']
    phone_number=PhoneNumberField()