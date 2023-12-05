from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Sign
from django.contrib.auth.models import User

def index(request):
    return render(request, 'store/index.html')

def about(request):
    return render(request, 'store/about.html')

def sign(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'store/sign.html', {'error_message': 'Username already taken'})

        user = User.objects.create_user(username, "", password)
        return render(request, 'store/login.html')

    return render(request, 'store/sign.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('cart')  
        else:
            return render(request, 'store/login.html', {'error_message': 'Invalid credentials'})
    return render(request, 'store/login.html')


def cart(request):
    return render(request, 'store/cart.html')
