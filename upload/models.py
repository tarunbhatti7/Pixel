from django.db import models
from django.core.validators import FileExtensionValidator
from User_profile.models import Profile
# Create your models here.


class Post_first(models.Model):
    name=models.CharField(max_length=20,blank=False,null=False)
    title=models.CharField(max_length=240)
    dis=models.CharField(max_length=240,blank=True,null=True)
    da_ti=models.DateTimeField(auto_now=True)
    file=models.FileField(upload_to='files',null=False ,blank=False ,max_length=100000 ,validators=[FileExtensionValidator( ['pdf' , 'doc' , 'jpeg'] ) ])
    auname=models.CharField(max_length=30,default='name')
    author=models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        max_length=100,
    )
    def __str__(self):
        return self.title

class Post_second(models.Model):
    name=models.CharField(max_length=20,blank=False,null=False)
    title=models.CharField(max_length=240)
    da_ti=models.DateTimeField(auto_now=True)
    dis=models.CharField(max_length=240,blank=True,null=True)
    file=models.FileField(upload_to='files',null=False ,blank=False ,max_length=100000,validators=[FileExtensionValidator( ['pdf', 'doc' ,'jpeg' ,'jpg'] ) ])
    auname=models.CharField(max_length=30,default='name')
    author=models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        max_length=100,
        
    )
    def __str__(self):
        return self.title

class Post_third(models.Model):
    name=models.CharField(max_length=20,blank=False,null=False)
    title=models.CharField(max_length=240)
    da_ti=models.DateTimeField(auto_now=True)
    dis=models.CharField(max_length=240,blank=True,null=True)
    file=models.FileField(upload_to='files',null=False ,blank=False ,max_length=100000,validators=[FileExtensionValidator( ['pdf', 'doc' ,'jpeg' , 'jpg'] ) ])
    auname=models.CharField(max_length=30,default='name')
    author=models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        max_length=100,
        
    )
    def __str__(self):
        return self.title
    

class Post_fourth(models.Model):
    name=models.CharField(max_length=20,blank=False,null=False)
    title=models.CharField(max_length=240)
    da_ti=models.DateTimeField(auto_now=True)
    dis=models.CharField(max_length=240,blank=True,null=True)
    file=models.FileField(upload_to='files',null=False ,blank=False ,max_length=100000,validators=[FileExtensionValidator( ['pdf','doc','jpeg' ,'jpg'] ) ])
    auname=models.CharField(max_length=30,default='name')
    author=models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        max_length=100,
        
    )
    def __str__(self):
        return self.title    

