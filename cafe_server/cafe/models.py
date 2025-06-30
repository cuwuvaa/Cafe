from django.db import models

# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=64)
    rating = models.IntegerField(max_length=10)

    def __str__(self):
        return f"{self.name} with rating: {self.rating}"