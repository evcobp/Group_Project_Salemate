from django.db import models
from login_reg_app.models import User

# Create your models here.

class TraitManager(models.Manager):
    pass
        
class Trait(models.Model):
    trait_one = models.BooleanField()
    trait_two = models.BooleanField()
    trait_three = models.BooleanField()
    trait_four = models.BooleanField()
    trait_five = models.BooleanField()
    trait_six = models.BooleanField()
    trait_seven = models.BooleanField()
    trait_eight= models.BooleanField()
    trait_nine = models.BooleanField()
    user_traits = models.ForeignKey(User,related_name="traits", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class Question(models.Model):
    question_one = models.BooleanField()
    question_two = models.BooleanField()
    question_three = models.BooleanField()
    question_four = models.BooleanField()
    question_five = models.BooleanField()
    user_responses = models.ForeignKey(User, related_name="questions", on_delete = models.CASCADE)
    