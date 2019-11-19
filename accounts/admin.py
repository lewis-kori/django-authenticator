from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model=User
    list_display=['username','email','phone_number']

admin.site.register(User,CustomUserAdmin)