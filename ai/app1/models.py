from django.db import models

# Create your models here.
class Home_page(models.Model):
    fname     = models.CharField(default="",max_length=150)
    lname     =models.CharField(default="",max_length=150)
    useremail = models.EmailField(default="",max_length=100)
    phone     = models.CharField(max_length=10,default="")
    password  = models.CharField(default="",max_length=100) 
    cpassword  = models.CharField(default="",max_length=100) 


    def  __str__(self):
        return self.fname
    