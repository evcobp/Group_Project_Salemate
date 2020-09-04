from django.db import models
from login_reg_app.models import User
from django import forms
import bcrypt


# Create your models here.
class BuyerTrait(models.Model):
    buyer_persistent = models.BooleanField()
    buyer_flexible = models.BooleanField()
    buyer_closer = models.BooleanField()
    buyer_consultative = models.BooleanField()
    buyer_detail_oriented = models.BooleanField()
    buyer_patient = models.BooleanField()
    buyer_charismatic = models.BooleanField()
    buyer_calculated = models.BooleanField()
    buyer_talker = models.BooleanField()
    buyer_traits = models.ForeignKey(User,related_name="buyer_traits", on_delete = models.CASCADE)
    buyer_created_at = models.DateTimeField(auto_now_add=True)
    buyer_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return {self.buyer_traits_id}



class BuyerTraitForm(forms.Form):
        model = BuyerTrait
        fields = ['buyer_persistent', 'buyer_flexible', 'buyer_closer', 'buyer_consultative','buyer_detail_oriented',
                  'buyer_patient', 'buyer_charismatic', 'buyer_calculated', 'buyer_talker']
        widgets = {
            'buyer_persistent': forms.BooleanField(required= False),
            'buyer_flexible' : forms.BooleanField(required=False),
            'buyer_closer' : forms.BooleanField(required=False),
            'buyer_consultative' : forms.BooleanField(required=False),
            'buyer_detail_oriented': forms.BooleanField(required=False),
            'buyer_patient' : forms.BooleanField(required=False),
            'buyer_charismatic' : forms.BooleanField(required=False),
            'buyer_calculated' : forms.BooleanField(required=False),
            'buyer_talker' : forms.BooleanField(required=False),
        }
        
class SellerTrait(models.Model):
    seller_persistent = models.BooleanField()
    seller_flexible = models.BooleanField()
    seller_closer = models.BooleanField()
    seller_consultative = models.BooleanField()
    seller_detail_oriented = models.BooleanField()
    seller_patient = models.BooleanField()
    seller_charismatic = models.BooleanField()
    seller_calculated = models.BooleanField()
    seller_talker = models.BooleanField()
    seller_traits = models.ForeignKey(User,related_name="seller_traits", on_delete = models.CASCADE)
    seller_created_at = models.DateTimeField(auto_now_add=True)
    seller_updated_at = models.DateTimeField(auto_now=True)

#class BuyerTraitForm(forms.Form):
 #       model = BuyerTrait
  #    widgets = {
   #         'buyer_persistent': forms.BooleanField(required=False),
    #        'buyer_flexible': forms.BooleanField(required=False),
    #        'buyer_closer': forms.BooleanField(required=False),
    ##        'buyer_consultative': forms.BooleanField(required=False),
    #        'buyer_detail_oriented': forms.BooleanField(required=False),
    #        'buyer_patient': forms.BooleanField(required=False),
    #       'buyer_charismatic': forms.BooleanField(required=False),
    #        'buyer_calculated': forms.BooleanField(required=False),
    #        'buyer_talker': forms.BooleanField(required=False),

