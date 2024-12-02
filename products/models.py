from django.db import models

class Drink(models.Model):
    name        = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    rating      = models.FloatField()
    
    def __str__(self):
        return self.name