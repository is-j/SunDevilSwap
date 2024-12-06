
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Profile
from django.contrib import messages
from mainApp.models import Item

# Create your views here.
def start(request):
    return render(request, "login/start.html")

def index(request):
    featured_items = Item.objects.all()[:8]  
    user = request.user
    first_name = user.first_name
    last_name = user.last_name

    context = {
        'first_name': first_name,
        'last_name': last_name,
    }
    return render(request, "main_page/main.html", {"first_name": request.user.first_name})

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'login/login.html')



def signUp_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')

        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email is already taken.')
            return redirect('signup')


        user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)


        Profile.objects.create(user=user)
        
        messages.success(request, f'Account created successfully. Welcome, {first_name}!')
        return redirect('login')

    return render(request, 'login/sign_up.html')


def home(request):
    return render(request, 'main/home.html')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item

def sell(request):
    if request.method == 'POST':

        item_name = request.POST.get('item_name')
        item_description = request.POST.get('item_description')
        item_price = request.POST.get('item_price')
        item_category = request.POST.get('item_category')
        item_image = request.FILES.get('item_image')

        item = Item.objects.create(
            description=item_name,
            price=item_price,
            cloth=True if item_category == 'clothes' else False,
            equip=True if item_category == 'lab_equipment' else False,
            text=True if item_category == 'textbooks' else False,
            image=item_image
        )
        item.save()

        return HttpResponse('<h1>Item successfully listed!</h1><a href="/sell/">Go Back</a>')

    return render(request, 'bsPage/sell_now.html')

def buy_now(request):
    category = request.GET.get('category')
    condition = request.GET.get('condition')
    search_query = request.GET.get('query')
    items = Item.objects.all()
    if category:
        if category == "Clothes":
            items = items.filter(cloth=True)
        elif category == "Lab Equipment":
            items = items.filter(equip=True)
        elif category == "Textbooks":
            items = items.filter(text=True)
    if condition:
        items = items.filter(condition=condition)
    if search_query:
        items = items.filter(description__icontains=search_query)

    return render(request, 'bsPage/buy_now.html', {'items': items})
