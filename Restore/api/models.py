from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=20, default="")
    last_name = models.CharField(max_length=20, default="")
    username = models.CharField(max_length=20, default="", unique=True)
    email = models.EmailField(max_length=50, default="", unique=True)
    password = models.CharField(max_length=12, default="")


class Tick_Tack_Toe(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE,)
    score =  models.DecimalField(
        max_digits=1000, decimal_places=0, default=0)
    
class Rock_Paper_Scissors(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE,)
    score =  models.DecimalField(
        max_digits=1000, decimal_places=0, default=0)
    
class Mario(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE,)
    score =  models.DecimalField(
       max_digits=1000, decimal_places=0, default=0)
    