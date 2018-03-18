from django.db import models

# Create your models here.

class formModel(models.Model):
	Name = models.CharField(max_length=256,blank=False)
	PhoneNumber = models.CharField(max_length=256,blank=False)
	Email= models.EmailField(blank=False)
	Message = models.CharField(max_length=1280)
