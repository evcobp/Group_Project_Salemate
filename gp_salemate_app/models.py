from django.db import models

# Create your models here.

class User(models.Model):
    pass

class BuyerTrait(models.Model):
    trait_one = models.BooleanField()
    trait_two = models.BooleanField()
    trait_three = models.BooleanField()
    trait_four = models.BooleanField()
    trait_five = models.BooleanField()
    trait_six = models.BooleanField()
    trait_seven = models.BooleanField()
    trait_eight= models.BooleanField()
    trait_nine = models.BooleanField()
    buyer_traits = models.ForeignKey(User,related_name="buyer_traits", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class BuyerQuestion(models.Model):
    question_one = models.BooleanField()
    question_two = models.BooleanField()
    question_three = models.BooleanField()
    question_four = models.BooleanField()
    question_five = models.BooleanField()
    buyer_responses = models.ForeignKey(User, related_name="buyer_questions", on_delete = models.CASCADE)
    
    
class SellerTrait(models.Model):
    trait_one = models.BooleanField()
    trait_two = models.BooleanField()
    trait_three = models.BooleanField()
    trait_four = models.BooleanField()
    trait_five = models.BooleanField()
    trait_six = models.BooleanField()
    trait_seven = models.BooleanField()
    trait_eight= models.BooleanField()
    trait_nine = models.BooleanField()
    seller_traits = models.ForeignKey(User,related_name="seller_traits", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class SellerQuestion(models.Model):
    question_one = models.BooleanField()
    question_two = models.BooleanField()
    question_three = models.BooleanField()
    question_four = models.BooleanField()
    question_five = models.BooleanField()
    seller_responses = models.ForeignKey(User, related_name="seller_questions", on_delete = models.CASCADE)
    