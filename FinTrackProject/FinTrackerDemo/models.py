from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username
    
class Account(models.Model):
    # could be used to set up the primary key manually
    # account_id = models.IntegerField(primary_key = True)
    userID = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 

    current_balance = models.DecimalField(max_digits=15, decimal_places=2)
    available_balance = models.DecimalField(max_digits=15, decimal_places=2)
    expenses = models.DecimalField(max_digits=15, decimal_places=2)
    earnings = models.DecimalField(max_digits=15, decimal_places=2)
    total_savings = models.DecimalField(max_digits=15, decimal_places=2)

class Savings(models.Model):
    # could be used to set up the primary key manually
    # savings_id = models.IntegerField(primary_key = True)
    accountID = models.ForeignKey(Account, on_delete=models.CASCADE) 

    total_savings = models.DecimalField(max_digits=15, decimal_places=2)
    investments = models.DecimalField(max_digits=15, decimal_places=2)
    goals = models.DecimalField(max_digits=15, decimal_places=2)

class Goal(models.Model):
    # could be used to set up the primary key manually
    # goal_id = models.IntegerField(primary_key = True)
    savingsID = models.ForeignKey(Savings, on_delete=models.CASCADE) 

    total_savings = models.DecimalField(max_digits=15, decimal_places=2)
    investments = models.DecimalField(max_digits=15, decimal_places=2)
    goals = models.DecimalField(max_digits=15, decimal_places=2)