from django.shortcuts import render
from login_reg_app.models import User
# from gp_salemate_app.models import Trait, Question
# from django.http import HttpResponseRedirect

# Create your views here.


def seller_profile_setup(request):
    context = {
        'user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, 'seller_profile_setup.html', context)

def seller_profile(request):
    context = {
        'user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, 'seller_profile_page.html', context)

def buyer_profile_setup(request):
    context = {
        'user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, 'buyer_profile_setup.html', context)

def buyer_profile(request):
    context = {
        'user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, 'buyer_profile_page.html', context)

def get_traits(request):
    pass
