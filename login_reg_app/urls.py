from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('buyer_reg_login/', views.buyer_reg_login),
    path('seller_reg_login/', views.seller_reg_login),
    path('create_user', views.create_user),
    path('login', views.login),
]
