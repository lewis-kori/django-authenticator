from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .forms import CustomUserCreationForm, LoginForm
from .models import User

def login_view(request):
    form=LoginForm(request.POST or None)
    
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        try:
            user=authenticate(username=User.objects.get(email=username),password=password)
        except:
            user=authenticate(username=username,password=password)
        login(request, user)
        return redirect('register')
    context={'form':form}
    return render(request,'login.html',context=context)
