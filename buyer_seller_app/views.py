from django.shortcuts import render, redirect
from login_reg_app.models import User
from .models import BuyerTrait, SellerTrait
from .forms import BuyerTraitForm
from django.core import mail
import bcrypt
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

def buyer_profile_setup(request, user_id):
    user_that_logged_in = User.objects.get(id=request.session['user_id'])
    user_traits = BuyerTrait.objects.filter(buyer_traits=user_that_logged_in).count()

    if user_traits != 0:
        context = {
        'user': User.objects.get(id=user_id),
    }
        return render(request, 'buyer_profile_setup.html', context)

def buyer_profile(request):
    user_that_logged_in = User.objects.get(id=request.session['user_id'])
    user_traits = BuyerTrait.objects.filter(buyer_traits=user_that_logged_in).count()

    if user_traits == 0:
        return render(request, 'buyer_profile_setup.html')
    
    context = {
        'user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, 'buyer_profile_page.html', context)

def get_traits(request):
    user_new_traits = BuyerTrait.objects.create(
                        buyer_persistent=request.method['POST'],
                        buyer_flexible=request.method['POST'],
                        buyer_closer=request.method['POST'],
                        buyer_consultative=request.method['POST'],
                        buyer_detail_oriented=request.method['POST'],
                        buyer_patient=request.method['POST'],
                        buyer_charismatic=request.method['POST'],
                        buyer_calculated=request.method['POST'],
                        buyer_talker=request.method['POST'])
    if request.method == "POST":
        form = BuyerTraitForm(request.POST)
        if form.is_valid():
            return user_new_traits

            #return render(request,'buyer_profile_page.html',context)
        #else:
           # form = BuyerTraitForm()
        #return render(request, 'buyer_profile_setup.html', {'form': form})

def buyer_trait_form(request):
    user_that_logged_in = User.objects.get(id=request.session['user_id'])
    buyer_trait = BuyerTrait(buyer_persistent= buyer_trait_form['buyer_persistent'], buyer_flexible=request.session['buyer_flexible'], 
                             buyer_closer= request.session['buyer_closer'], buyer_consultative= request.session['buyer_consultative'],
                             buyer_detail_oriented= request.session['buyer_detail_oriented'], buyer_patient= request.session['buyer_patient'],
                             buyer_relatable= request.session['buyer_relatable'],buyer_calculated= request.session['buyer_calculated'],
                             buyer_talker= request.session['buyer_talker'])
    user_trait = user_that_logged_in.buyer_trait.save()
    context = {
        'user_trait': BuyerTrait.objects.all()
    }
    return render(request, 'buyer_profile_page.html', context)
        
def buyer_trait_form_two(request):
    buyer_persistent = BuyerTrait.objects.get(request.POST['buyer_persistent'])
    context = {
            'buyer_persistent': buyer_persistent, 
            'buyer_flexible': buyer_flexible,
            'buyer_closer': request.POST['buyer_closer'], 
            'buyer_consultative': request.POST['buyer_consultative'],
            'buyer_detail_oriented': request.POST['buyer_detail_oriented'], 
            'buyer_patient': request.POST['buyer_patient'],
            'buyer_relatable': request.POST['buyer_relatable'],
            'buyer_calculated': request.POST['buyer_calculated'],
            'buyer_talker': request.POST['buyer_talker']
            }
    return render(request, 'buyer_profile_page.html', context)

def traits_page(request):
    return render(request, 'buyer_profile_page.html')

def profile_setup_page(request):
    return render(request, 'buyer_profile_setup.html')

def send_email(self, user_that_logged_in):
    connection = mail.get_connection()
    connection.open()

    from_email = user_that_logged_in.email
    match_email = user_that_logged_in.match.email
    email_one = mail.EmailMessage(
            'We are a Match on Salemate!',
            "Let's make this an enjoyable buying cycle!",
            "from_email",
            "match_email",
            connection=connection,
            fail_silently=False,
    )
    email_one.send()
