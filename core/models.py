import email
from django.db import models

# Create your models here.
class Profile(models.Model):
    email =models.TextField()
    name =models.TextField()
    dob =models.DateField()
    gender =models.TextField()
    phone =models.TextField()
    course = models.TextField()
    
