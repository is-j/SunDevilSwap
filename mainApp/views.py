from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login




from mainApp.models import Item

# Create your views here.
def index(request):
    featured_items = Item.objects.all()[:8]  
    return render(request, "main_page/main.html", {"featured_items": featured_items})

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'login/login.html')

def signUp_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')

        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email is already taken.')
            return redirect('signup')

        user = User.objects.create_user(username=email, password=password)
        Profile.objects.create(user=user)  # Create profile for the user
        messages.success(request, 'Account created successfully.')
        return redirect('login')
    return render(request, 'login/signup.html')

def home(request):
    return render(request, 'main/home.html')

def sell(request):
    return render(request, 'bsPage/sell_now.html')