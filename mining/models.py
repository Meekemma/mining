import random
import string
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.utils.functional import cached_property

# Create your models here.
GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

class Profile(models.Model):      
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    birth_date = models.DateField(null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=200, null=True, unique=True)
    profile_pic = models.ImageField(blank=True,null=True, default='profile.jpg', upload_to='profile_pic/')
    country = CountryField(null=True)
    state = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return str(self.user)
    

    


class Cryptocurrency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    current_price = models.DecimalField(max_digits=15, decimal_places=2)
    mining_difficulty = models.DecimalField(max_digits=15, decimal_places=2)
    # Add other cryptocurrency-related fields as needed

    def __str__(self):
        return f"Cryptocurrency {self.name} by {self.current_price}"






class Referral(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='referrals_received')
    referral_code = models.CharField(max_length=7, unique=True, blank=True)
    referrer =models.ForeignKey(Profile, on_delete=models.CASCADE,  related_name='referrals_made', blank=True, null=True)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0.00,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Referral'
        verbose_name_plural = 'Referrals'
        ordering = ['-created_at']

    def __str__(self):
        profile_username = self.profile.user.username if self.profile else "Unknown"
        referrer_username = self.referrer.user.username if self.referrer else "Unknown"
        return f"Referral for {profile_username} by {referrer_username}"   



class MiningStatus(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
    mining_power = models.DecimalField(max_digits=15, decimal_places=2)
    mining_progress = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    # Add other mining status-related fields as needed



class MiningHistory(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
    mined_amount = models.DecimalField(max_digits=15, decimal_places=2)
    mined_date = models.DateTimeField(auto_now_add=True)
    # Add other mining history-related fields as needed

class Balance(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Balance: {self.amount}"


status_choices = (
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('X', 'Canceled'),
    )
class Withdrawal(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    balance = models.ForeignKey(Balance, on_delete=models.CASCADE,blank=True, null=True)
    withdrawal_amount = models.DecimalField(max_digits=15, decimal_places=2)
    wallet=models.CharField(max_length=100, blank=True, null=True)
    pin=models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1, choices=status_choices, default='P')
    withdrawal_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-withdrawal_date']

    def __str__(self):
        return f"Withdrawal of {self.withdrawal_amount} by {self.profile}"
    



status_choices = (
        ('P', 'Pending'),
        ('C', 'Completed'),
    )

class Deposit(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    balance = models.ForeignKey(Balance, on_delete=models.CASCADE,blank=True, null=True)
    deposit_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=1, choices=status_choices, default='P')
    deposit_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-deposit_date']

    def __str__(self):
        return f"Deposit of {self.deposit_amount} by {self.profile}"  
    
    
    
       
    

class Invoice(models.Model):
    STATUS_CHOICES = ((-1,"Not Started"),(0,'Unconfirmed'), (1,"Partially Confirmed"), (2,"Confirmed"))

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    deposit = models.ForeignKey(Deposit, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES, default=-1)
    order_id = models.CharField(max_length=250)
    address = models.CharField(max_length=250, blank=True, null=True)
    btcvalue = models.IntegerField(blank=True, null=True)
    received = models.IntegerField(blank=True, null=True)
    txid = models.CharField(max_length=250, blank=True, null=True)
    rbf = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"Invoice for Order {self.order_id} - Address: {self.address}"


class Contact(models.Model):
    name= models.CharField(max_length=200)
    email=models.EmailField()
    body=models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    class Meta:
        ordering = ['-created_on']


    def __str__(self):
        return self.name
    
    
class Testimony(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField()
    content=models.CharField(max_length=500)
    like=models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name
    