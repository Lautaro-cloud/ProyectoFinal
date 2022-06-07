from operator import truediv
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User


class BlogModel(models.Model):
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=100)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Categorias(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField('Nombre de la Categoria',max_length= 100, null= False,blank= False)
    estado = models.BooleanField('Categoria Activada/Categoria no Activada', default = True)
    fecha_creacion = models.DateField('Fecha de Creacion',auto_now = False,auto_now_add = True)

    class Meta:
        verbose_name ='Categorias'
    def __str__(self):
        return self.nombre

class Autor(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField('Nombre de Autor',max_length= 100, null= False,blank= False)
    apellido = models.CharField('Apellido de Autor',max_length= 100, null= False,blank= False)
    facebook = models.URLField('Facebook', null = True, blank = True)
    twitter = models.URLField('Twitter', null = True, blank = True)
    instagram = models.URLField('Instagram', null = True, blank = True)
    web = models.URLField('Web', null = True, blank = True)
    email = models.EmailField('Correo Electronico', blank = False, null = True)
    estado = models.BooleanField('Autor Activo/No Activo',default = True)
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
    def __str__(self):
        return "{0},{1}".format(self.apellido, self.nombre)

