from django.db import models

# Create your models here.
class User(models.Model):
    # could be used to set up the primary key manually
    # user_id = models.IntegerField(primary_key = True)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=50) 
    password = models.CharField(max_length=50)

class Account(models.Model):
    # could be used to set up the primary key manually
    # account_id = models.IntegerField(primary_key = True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) 

    current_balance = models.DecimalField(max_digits=15, decimal_places=2)
    available_balance = models.DecimalField(max_digits=15, decimal_places=2)
    expenses = models.DecimalField(max_digits=15, decimal_places=2)
    earnings = models.DecimalField(max_digits=15, decimal_places=2)
    total_savings = models.DecimalField(max_digits=15, decimal_places=2)

class Savings(models.Model):
    # could be used to set up the primary key manually
    # savings_id = models.IntegerField(primary_key = True)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE) 

    total_savings = models.DecimalField(max_digits=15, decimal_places=2)
    investments = models.DecimalField(max_digits=15, decimal_places=2)
    goals = models.DecimalField(max_digits=15, decimal_places=2)

class Goal(models.Model):
    # could be used to set up the primary key manually
    # goal_id = models.IntegerField(primary_key = True)
    savings_id = models.ForeignKey(Savings, on_delete=models.CASCADE) 

    total_savings = models.DecimalField(max_digits=15, decimal_places=2)
    investments = models.DecimalField(max_digits=15, decimal_places=2)
    goals = models.DecimalField(max_digits=15, decimal_places=2)