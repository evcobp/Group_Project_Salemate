from django.contrib import admin
from buyer_seller_app.models import Trait
from .models import User
# Register your models here.
admin.site.register(User)
admin.site.register(Trait)
