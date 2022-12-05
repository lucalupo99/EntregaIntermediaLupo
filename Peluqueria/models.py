from django.db import models

# Create your models here.

class Turno(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    Telefono= models.IntegerField()

    def __str__(self):
        return self.nombre+" "+self.apellido

class Cliente(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    documento= models.IntegerField()

    def __str__(self):
        return self.nombre+" "+self.apellido
    
class Producto(models.Model):
    nombre= models.CharField(max_length=50)
    producto= models.CharField(max_length=50)
    marca= models.CharField(max_length=50)
    telefono= models.IntegerField()
   
    def __str__(self):
        return self.nombre+" "+self.marca



    
