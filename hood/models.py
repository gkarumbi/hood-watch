from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=200,blank=True)
    contact_info = models.CharField(max_length=200,blank=True)
    profile_Id = models.IntegerField(default=0)
    profile_picture = models.ImageField(upload_to='users/', default='user.png')
    bio = models.TextField(default="Welcome!")


    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_location(self, location):
        self. location = location
        self.save()

    def update_bio(self,bio):
        self.bio = bio
        self.save()  

    def __str__(self):
        return f'{self.user.username} Profile' 
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

class Neighbourhood(models.Model):
    hood_name = models.CharField(max_length=50 )
    location = models.CharField(max_length=50 )
    occupants = models.IntegerField(default=0)
    admin = models.OneToOneField(User,unique = True , on_delete=models.CASCADE,null=True,default=True)    
    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    def update_neighbourhood(self):
        self.save()
    
    def update_occupants(self):
        self.save()

    def __str__(self):
        return self.location

class Businesses(models.Model):
    business_name = models.CharField(max_length=100)
    business_email = models.EmailField()
    bussiness_description= models.TextField(default=True)
    neighbourhood=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE, null=True)
    logo = models.ImageField(upload_to='media/', blank = True, null =True)
    # user = models.OneToOneField(Profile, default=True,on_delete=models.CASCADE,null=True)


    def create_business(self):
        self.save()

    def delete_business(self):
        self.save()

    def update_business(self):
        self.save()

    def __str__(self):
        return self.business_name


class Post(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField(max_length=250)
    address = models.CharField(max_length=30)
    def __str__(self):
        return f'{self.title}'

      
    def save_post(self):
        self.save()