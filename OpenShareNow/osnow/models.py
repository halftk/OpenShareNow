from django.db import models

# Create your models here.
class Item(models.Model):
	nom = models.TextField(max_length=100)
	descripcio = models.TextField(max_length=1000)
	link= models.TextField(max_length=500)
	dataCreacio= models.DateTimeField()
	dataModificacio= models.DateTimeField()
	usuari= models.IntegerField()
	tipus = models.IntegerField()
	valoracio= models.IntegerField()

class Tipus(models.Model):
	nom = models.TextField(max_length=100)
	descripcio = models.TextField(max_length=500)

class Categories(models.Model):
	nom = models.TextField(max_length=100)
	descripcio = models.TextField(max_length=500)

class Categoria_aux(models.Model):
	categoria = models.IntegerField()
	item = models.IntegerField()

class Usuaris(models.Model):
	login = models.TextField(max_length=15)
	pwd = models.TextField(max_length=25)
	email = models.TextField(max_length=30)
	avatar = models.TextField(max_length=30)
	sexe = models.IntegerField(max_length=1)
	dataAlta= models.DateTimeField()
	dataNeixement= models.DateTimeField()

class Comentaris(models.Model):
	text = models.TextField(max_length=100)
	dataCreacio = models.DateTimeField()
	dataModificacio = models.DateTimeField()
	usuari = models.IntegerField()
	item = models.IntegerField()

class Comentaris_aux(models.Model):
	comentari= models.IntegerField()
	resposta= models.IntegerField()

class Idioma(models.Model):
	nom = models.TextField(max_length=30)
	imatge = models.TextField(max_length=30)

class Idioma_aux(models.Model):
	item = models.IntegerField()
	idioma = models.IntegerField()

class Tags(models.Model):
	nom = models.TextField(max_length=100)

class Tags_aux(models.Model):
	item = models.IntegerField()
	tag = models.IntegerField()

class Valoracio(models.Model):
	item = models.IntegerField()
	usuari = models.IntegerField()
	nota = models.IntegerField(max_length=2)

