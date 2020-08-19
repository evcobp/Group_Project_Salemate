from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/buyer/ -> views.dashboard
    path('', views.dashboard),
]
