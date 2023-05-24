from django.contrib import messages, auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from credentials.forms import CustomUserCreationForm





def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':

        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Registered successfully")
            return redirect('credentials:login')
        else:
            form = CustomUserCreationForm()
    return render(request, 'register.html',{'form':form})



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
                auth.login(request,user)
                messages.info(request, "successfully logged in")
                return render(request,'store.html')
        else:
                messages.info(request,"Invalid login credentials")
                return render(request,'login.html')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')