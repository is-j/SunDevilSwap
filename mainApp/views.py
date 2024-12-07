
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages
from mainApp.models import Item, Cart
from django.db.models import Sum
from django.contrib.messages import get_messages



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
    storage = get_messages(request)
    for _ in storage:
        pass
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

    storage = get_messages(request)
    for _ in storage:
        pass

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

        messages.success(request, 'Your item has been listed successfully.')

    return render(request, 'bsPage/sell_now.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def profile(request):
    # Fetch the logged-in user's profile
    profile = request.user.profile

    if request.method == 'POST':

        email = request.POST.get('email', profile.email)
        address = request.POST.get('address', profile.address)
        phone = request.POST.get('phone', profile.phone)
        profile.email = email
        profile.address = address
        profile.phone = phone
        profile.save()

        user = request.user
        user.email = email
        user.save()


        messages.success(request, "Your profile has been updated successfully!")
        return redirect('profile')

    return render(request, 'login/profile.html', {'profile': profile})

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
def item_detail_view(request, item_id):
    item = get_object_or_404(Item, itemID=item_id)
    return render(request, "bsPage/item_detail.html", {"item": item})
@login_required

def add_to_cart(request, item_id):
    if request.method == "POST":

        item = get_object_or_404(Item, itemID=item_id)
        
        user = request.user

        cart_item, created = Cart.objects.get_or_create(user=user, item=item, defaults={
            'image': item.image,
            'price': item.price,
            'payment': 'NoPayment',
            'quantity': 1,
        })

        if not created:

            cart_item.quantity += 1
            cart_item.save()

        return redirect('cart_detail')  #


@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.price * item.quantity for item in cart_items)  # Use quantity for total
    return render(request, 'bsPage/cart.html', {'cart_items': cart_items, 'total_price': total_price})


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

    # Exclude items that are already purchased
    items = items.exclude(cart_entries__payment="Completed")

    return render(request, 'bsPage/buy_now.html', {'items': items})

@login_required
def process_payment(request):
    if request.method == 'POST':
        # Fetch cart items for the user
        cart_items = Cart.objects.filter(user=request.user)
        total_price = cart_items.aggregate(total=Sum('price'))['total']

        payment_successful = True  # Simulate a successful payment
        if payment_successful:
            # Mark items as paid and remove them from the cart
            for cart_item in cart_items:
                cart_item.payment = 'Completed'
                cart_item.save()
                # Remove item from the selling list
                cart_item.item.delete()

            # Clear the user's cart
            cart_items.delete()
            messages.success(request, "Payment successful!")
            return redirect('thank_you')  # Redirect to the thank-you page
        else:
            messages.error(request, "Payment failed. Please try again.")
            return redirect('cart_detail')

def thank_you(request):
    return render(request, 'bsPage/thank_you.html')
