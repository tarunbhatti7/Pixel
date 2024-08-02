from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=30)
    disc = models.CharField(max_length=255)
    image = models.ImageField(max_length=255,upload_to='teams' , default='{%static /user.png%}')
    
    def __str__(self):
        return self.name

class Bugs(models.Model):
    email = models.EmailField(max_length=100 )
    name = models.CharField(max_length=50)
    bug = models.CharField(max_length=255)
    image = models.ImageField(max_length=255,upload_to='bugs',null=True,blank=True)
    def __str__(self):
        return self.name