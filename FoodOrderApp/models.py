from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    region = models.CharField(max_length=20)
    taste = models.CharField(max_length=20)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    food = models.ForeignKey(Food,on_delete=models.CASCADE)
    name = models.CharField(max_length=20,default="")
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)

