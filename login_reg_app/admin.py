from django.contrib import admin
from buyer_seller_app.models import BuyerTrait, SellerTrait
from .models import User
# Register your models here.
admin.site.register(User)
admin.site.register(BuyerTrait)
admin.site.register(SellerTrait)

