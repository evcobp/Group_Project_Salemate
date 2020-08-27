from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('seller_profile_page', views.seller_profile_page),
]