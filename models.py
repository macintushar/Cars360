from django.db import models

# Create your models here.

class Names(models.Model):
    make = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    cost = models.IntegerField()
    
    class Meta:
        db_table = 'Cars'
    