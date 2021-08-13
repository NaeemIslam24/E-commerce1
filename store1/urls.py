from django.urls import path
from . import views

app_name = 'store1'

urlpatterns = [

    path('', views.index, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]
