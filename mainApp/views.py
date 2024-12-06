from django.http import HttpResponse
from django.shortcuts import render

from mainApp.models import Item

# Create your views here.
def index(request):
    featured_items = Item.objects.all()[:8]  
    return render(request, "main_page/main.html", {"featured_items": featured_items})

def home(request):
    return render(request, 'main/home.html')

def sell(request):
    return render(request, 'bsPage/sell_now.html')