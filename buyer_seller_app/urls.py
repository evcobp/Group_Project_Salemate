from django.urls import path
from . import views


urlpatterns = [
    #localhost:8000/buyer
    path('buyer', views.buyer_profile),
    path('seller', views.seller_profile),
    path('buyer_profile_setup/<int:user_id>', views.buyer_profile_setup),
    path('seller_profile_setup/<int:user_id>', views.buyer_profile_setup),
    path('seller_profile', views.seller_profile),
    path('buyer_profile', views.seller_profile),
]
