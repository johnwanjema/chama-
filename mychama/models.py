from django.db import models
import datetime as dt
from django.contrib.auth.models import User
# Create your models here.
class Group(models.Model):
    group_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='photos')
    description = models.CharField(max_length=255)
    Adress = models.EmailField(blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('group_name',)
    

    def __str__(self):
        return self.group_name


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