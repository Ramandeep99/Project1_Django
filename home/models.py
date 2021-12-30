from django.db import models

# Create your models here.
class User(models.Model):
    Username = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    Phoneno = models.IntegerField()
    password = models.CharField(max_length=10)
    date = models.DateField()

