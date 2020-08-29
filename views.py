from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from gp_salemate_app.models import Trait, Question

# Create your views here.
def seller_profile_setup(request):
    return render(request, 'seller_profile_setup.html')

def seller_profile_page(request):
    return render(request, 'seller_profile_page.html')

def buyer_profile_setup(request):
    return render(request, 'buyer_profile_setup.html')

def buyer_profile_page(request):
    return render(request, 'buyer_profile_page.html')

def get_traits(request):
    pass
