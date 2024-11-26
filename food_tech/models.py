
from django.db import models
from django.contrib.auth.models import User

class FoodWasteReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    waste_amount = models.PositiveIntegerField()  # Amount of food wasted in grams
    food_type = models.CharField(max_length=100)  # Type of food wasted
    report_date = models.DateTimeField(auto_now_add=True)
    is_recycled = models.BooleanField(default=False)  # Whether the food waste is recycled

class FoodRecoveryEffort(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_donated = models.PositiveIntegerField()  # Amount of food donated in grams
    recovery_date = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    total_food_wasted = models.PositiveIntegerField(default=0)  # Total food wasted by the user
    total_food_donated = models.PositiveIntegerField(default=0)  # Total food donated by the user
