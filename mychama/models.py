from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Group(models.Model):
    groupName = models.CharField(max_length=255, unique=True)
    paybillNo = models.PositiveIntegerField(unique=True)
    contribution_amnt = models.DecimalField(
        max_digits=10, decimal_places=2)
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='chama', through='Membership', blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='admin')
    PAYMENT_TYPE = (
        ('D', 'Daily'),
        ('W', 'Weekly'),
        ('M', 'Monthly'),
        ('Q', 'Quartely')
    )
    contribution_interval = models.CharField(max_length=1, choices=PAYMENT_TYPE,
                                             blank=True, default='d', help_text='Contribution Intervals')

    class Meta:
        ordering = ['groupName']

    def __str__(self):
        return self.groupName


class Individual(models.Model):
    name = models.CharField(max_length=150)
    avartar = models.ImageField(upload_to='photos')
    contact_adress = models.CharField(max_length=150)
    EmailAdress = models.EmailField(blank=True)
    natinal_id = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    registration_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name

class Group_member(models.Model):
    member_name = models.CharField(max_length=150)
    contact_adress = models.CharField(max_length=150)
    natinal_id = models.CharField(max_length=150)
    image = models.ImageField(upload_to='photos')
    contact_adress = models.CharField(max_length=150)
    EmailAdress = models.EmailField(blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group)



    class Meta:
        ordering = ('member_name',)


class Group_contribution(models.Model):
    Amount_contributed = models.CharField(max_length=150)
    contribution_date = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group)
    

    class Meta:
        ordering = ('group',)


    def __str__(self):
        return self.group.group_name

class Individual_contribution(models.Model):
    Amount_contributed = models.CharField(max_length=150)
    contribution_date = models.DateTimeField(auto_now_add=True)
    individual = models.ForeignKey(Individual)

    class Meta:
        ordering = ('individual',)
    

    def __str__(self):
        return self.individual.name

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profiles/')
    bio = models.CharField(max_length=250)
    email = models.EmailField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['bio']

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Membership(models.Model):
    member = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, on_delete=models.CASCADE)
    chama = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=False)



