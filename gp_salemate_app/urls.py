from django.urls import path, include
from . import views


urlpatterns = [
    path('buyer_profile_setup', views.buyer_profile_setup, name="buyer_profile_setup"),
    path('buyer_profile_page', views.buyer_profile_page, name="buyer_profile_page"),
    path('seller_profile_setup', views.seller_profile_setup, name="seller_profile_setup"),
    path('seller_profile_page', views.seller_profile_page, name='seller_profile_page'),
    path('seller_traits', views.seller_traits, name='seller_traits')
]