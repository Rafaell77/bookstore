from django.db import models
from django.contrib.auth.models import User

 class Order(models.Model):
     product = models.ManyToManyField(product, blank=False)
     user = models.ForeignKey(User, on_delete=models.CASCADE) 

