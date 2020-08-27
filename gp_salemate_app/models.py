from django.db import models

# Create your models here.
class BuyerTrait(models.Model):
    Persistent = 'TRAIT_ONE',
    Flexible = 'TRAIT_TWO',
    Closer = 'TRAIT_THREE',
    Detail_Oriented = 'TRAIT_FOUR',
    Patient = 'TRAIT_FIVE',
    Relatable = 'TRAIT_SIX',
    Calculated = 'TRAIT_SEVEN',
    Talker = 'TRAIT_EIGHT',
    Consultative = 'TRAIT_NINE'
        
    BUYER_TRAIT_CHOICES = [
        (Persistent, 'Persistent')
        (Flexible, 'Flexible')
        (Closer,'Closer')
        (Detail_Oriented, 'Detail-Oriented')
        (Patient, 'Patient')
        (Relatable, 'Relatable')
        (Calculated, 'Calculated')
        (Talker, 'Talker')
        (Consultative,'Consultative')
    ]
    profile_selection = models.CharField(
        choices=BUYER_TRAIT_CHOICES
    )