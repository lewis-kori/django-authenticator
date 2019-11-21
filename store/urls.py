"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django_registration.backends.one_step.views import RegistrationView
from django.urls import path,include
from accounts import views,forms

urlpatterns = [
    path('admin/', admin.site.urls),

    # route to api for authentication and registration
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # handle custom user model registration form
    path('',RegistrationView.as_view(
             form_class=forms.CustomUserCreationForm,
             template_name='registration.html',
             success_url="login",
             ), name="register"),
    path("accounts/",include("django_registration.backends.one_step.urls")),
    path("accounts/",include("django.contrib.auth.urls")),
    path('login/',views.login_view,name='login'),

]
