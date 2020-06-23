from django.shortcuts import render,HttpResponseRedirect
from .forms import LoginForm,RegisterForm
from django.contrib.auth import login,logout,get_user_model
# Create your views here.

User = get_user_model()

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('email')
        user = User.objects.get(username=username)
        login(request,user)
        return HttpResponseRedirect('/')
    return render(request,'accounts/login.html',{'form':form})

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(username=username,password=password,email=username)
        login(request,user)
        return HttpResponseRedirect('/')
    return render(request,'accounts/register.html',{'form':form})
        

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')