from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from gp_salemate_app.models import BuyerTrait, BuyerQuestion, SellerTrait, SellerQuestion

# Create your views here.
def seller_profile_setup(request):
    return render(request, 'seller_profile_setup.html')

def seller_profile_page(request):
    traits = ['trait_one.trait','trait_two.trait','trait_three.trait','trait_four.trait','trait_five.trait',
              'trait_six.trait','trait_seven.trait','trait_eight.trait','trait_nine.trait']
    for trait in traits:
        if trait : True
        {trait}
    return render(request, 'seller_profile_page.html')
        
        #context = {
            #'trait_one': request.POST('trait_one'),
            #'trait_two': request.POST('trait_two'),
            #'trait_three': request.POST('trait_three'),
            #'trait_four': request.POST('trait_four'),
            #'trait_five': request.POST('trait_five'),
            #'trait_six': request.POST('trait_six'),
            #'trait_seven': request.POST('trait_seven'),
            #'trait_eight': request.POST('trait_eight'),
            #'trait_nine': request.POST('trait_nine'),
            
        #}
        #return render(request, 'seller_profile_page.html')

def buyer_profile_setup(request):
    return render(request, 'buyer_profile_setup.html')

def buyer_profile_page(request):
    traits = ['trait_one.trait','trait_two.trait','trait_three.trait','trait_four.trait','trait_five.trait',
              'trait_six.trait','trait_seven.trait','trait_eight.trait','trait_nine.trait']
    
    for trait in traits:
        if trait : True
        {trait}
        return render(request, 'buyer_profile_page.html')

def seller_traits(request):
    seller_trait = SellerTrait.objects.create(
        'trait_one','trait_two','trait_three','trait_four','trait_five','trait_six','trait_seven','trait_eight','trait_nine',   
    )
    
    context = {
        SellerTrait.objects.all()
    }
    return redirect(request, 'seller_profile_page', context)
