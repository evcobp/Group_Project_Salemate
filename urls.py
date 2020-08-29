from django.urls import path, include
from . import views


urlpatterns = [
    path('buyer_profile_setup', views.buyer_profile_setup),
    path('seller_profile_page', views.seller_profile_page),
    path('buyer_profile_page', views.get_traits)
]