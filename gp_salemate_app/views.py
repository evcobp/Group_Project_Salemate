from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def seller_profile_page(request):
    return render(request, 'seller_profile_page.html')


def buyer_traits(request):
    context = {
        {% for }
    }
    return render()