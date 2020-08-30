from django.shortcuts import render
from login_reg_app.models import User

# Create your views here.

def dashboard(request):
    user_that_logged_in = User.objects.get(id=request.session['user_id'])
    if Handicap.objects.filter(user=user_that_logged_in).count() == 0:
        Handicap.objects.create(
            user=user_that_logged_in,
            handicap_index=99.00
        )

    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'courses': Course.objects.all(),
        'tees': Tee.objects.all(),
        'handicap': Handicap.objects.get(user=user_that_logged_in),
        'scores': Score.objects.filter(user=user_that_logged_in),
    }
    return render(request, 'dashboard.html', context)
