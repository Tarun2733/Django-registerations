from django.shortcuts import render,redirect

from django.contrib.auth.forms import authenticate, login, logout
from .forms import UserCreationForm, LoginForm


# Create your views here.

#Home page
def index(request):
    return render(request, 'index.html')

#Login page
def user_login(request):
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password= form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})

#Signup page
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
        

#Logout page
def user_logout(request):
    logout(request)
    return redirect('login')