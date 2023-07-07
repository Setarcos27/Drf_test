from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description=models.TextField()
    tech= models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)
    
    