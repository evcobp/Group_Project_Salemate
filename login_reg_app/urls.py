from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('buyer_reg_login/', views.buyer_reg_login),
    path('seller_reg_login/', views.seller_reg_login),
    # path('create_user', views.create_user),
    path('create_user_buyer', views.create_user_buyer),
    path('create_user_seller', views.create_user_seller),
    # path('login', views.login),
    path('buyer_login', views.buyer_login),
    path('seller_login', views.seller_login),
]
