from django.db import models
import datetime


# Create your models here.
class registration(models.Model):
    name = models.CharField(max_length=20)
    player_1 = models.CharField(max_length=20, default="")
    player_2 = models.CharField(max_length=20, default="")
    player_3 = models.CharField(max_length=20, default="")
    player_4 = models.CharField(max_length=20, default="")
    team_name =  models.CharField(max_length=20, default="")
    email = models.EmailField(max_length=35)
    members = models.CharField(max_length=2,default="")
    whatsapp = models.IntegerField()

    def __str__(self):
        return self.name
    

class event(models.Model):
    title = models.CharField(max_length=50)
    game = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    desc= models.CharField(max_length = 50, default="")
    image_name = models.CharField( max_length=20 )
    images = models.ImageField(upload_to='static/')
    descord = models.CharField(max_length=200,default="")

    def __str__(self):
        return self.title

class banner(models.Model):
    title = models.CharField(max_length=50)
    game = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    desc= models.CharField(max_length = 50, default="")
    image_name = models.CharField( max_length=20 )
    images = models.ImageField(upload_to='static/')
    whatsapp_group = models.CharField(max_length=200,default="")

    def __str__(self):
        return self.title

class winners(models.Model):
    player_name = models.CharField(max_length=50)
    player_profile = models.ImageField(upload_to='static/')
    profile_name = models.CharField(max_length=50, default="")
    game = models.CharField( max_length=50)
    desc = models.CharField( max_length=50)
