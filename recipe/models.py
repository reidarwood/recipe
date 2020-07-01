from django.db import models
from django.utils import timezone

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published', 
        default=timezone.now)
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    amount = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    priority = models.IntegerField()
    description = models.CharField(max_length=200)
    
    class Meta:
        ordering = ['priority']
    
    def __str__(self):
        return self.description
    
