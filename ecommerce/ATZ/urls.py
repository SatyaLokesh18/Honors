from django.urls import path
from django.shortcuts import render
from .views import search

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.ATZ, name=""),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('login/', views.login, name="login"),
    path('login/signup', views.signup, name="signup"),
    path('search/', search, name='search'),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

]

