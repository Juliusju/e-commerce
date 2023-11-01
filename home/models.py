from django.db import models

# Create your models here.
from django.db import models

class MenTop(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20)
    quantity = models.IntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='mentop_images/')  # Add this line
    time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
    
class LadiesClothing(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20)
    quantity = models.IntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='ladies_clothings/') 
    time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
    
class MenSneakers(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20)
    quantity = models.IntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='ladies_clothings/') 
    time = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name
    
    

