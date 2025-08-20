from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, 'index.html')



def base_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('base_signup')
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('base_signup')
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            messages.success(request, "User created successfully")
            return redirect('login')
    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('base_signup')