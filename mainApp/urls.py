from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signUp_view, name='signup'),
    path('sell/', views.sell, name='sell'),  # Seller page
    path('start/', views.start,name='start'),
    path('buy/', views.buy_now, name="buy_now"),
    path("item/<int:item_id>/", views.item_detail_view, name="item_detail"),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_detail'),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('thank_you', views.thank_you, name="thank_you"),

   # path('sell/', views.sell_item, name='sell_item'),
    
]