from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    username = models.CharField(max_length=10,unique=True)
    email = models.EmailField()
    rut = models.CharField(max_length=10)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    password = models.CharField()
    telefono = models.CharField(default=0)
    


    def save(self, *args, **kwargs):
        self.username = self.rut  
        super().save(*args, **kwargs)