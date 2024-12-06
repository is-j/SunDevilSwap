from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signUp_view, name='signup'),
    path('sell/', views.sell, name='sell'),  # Seller page
   # path('sell/', views.sell_item, name='sell_item'),
    
]