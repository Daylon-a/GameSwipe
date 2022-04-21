from typing import Iterable
from django.db import models
from django.db.models import IntegerField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class GameData(models.Model):
    gameno = models.AutoField(primary_key=True, unique=True)
    gname = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    tags = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField()
    rating = models.SmallIntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    img = models.ImageField(upload_to='pics')

