from django.contrib.auth.models import AbstractUser,UserManager
from django.db.models import Q
from phonenumber_field.modelfields import PhoneNumberField

class CustomUserManager(UserManager):
    def get_by_natural_key(self,username):
        return self.get(
            Q(**{self.model.USERNAME_FIELD:username}) |
            Q(**{self.model.EMAIL_FIELD:username})
        )


class User(AbstractUser):
    objects=CustomUserManager()
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'phone_number']
    phone_number=PhoneNumberField()