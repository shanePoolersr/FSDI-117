from django.db import models
# from django.db import models

# Create your models here.
class Tech(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Experience(models.Model):
    entity = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    period = models.CharField(max_length=50)
    technologies = models.ManyToManyField(Tech)

    def __str__(self):
        return f"{self.title} at {self.entity}" 
    
   
