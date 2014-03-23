from django.db import models

# Create your models here.
class Seccio(models.Model):
	nom = models.TextField(max_length=100)
	descripcio = models.TextField(max_length=500)

class Categoria(models.Model):
	nom = models.TextField(max_length=100)
	descripcio = models.TextField(max_length=500)

class Usuari(models.Model):
	login = models.TextField(max_length=15)
	pwd = models.TextField(max_length=25)
	email = models.TextField(max_length=30)
	avatar = models.TextField(max_length=30)
	sexe = models.IntegerField(max_length=1)
	dataAlta= models.DateTimeField()
	dataNeixement= models.DateTimeField()

class Item(models.Model):
	nom = models.TextField(max_length=100)
	descripcio = models.TextField(max_length=1000)
	link= models.TextField(max_length=500)
	dataCreacio= models.DateTimeField()
	dataModificacio= models.DateTimeField()
	usuari= models.ForeignKey(Usuari)
	seccio = models.ForeignKey(Seccio)
	valoracio= models.IntegerField()

class Comentari(models.Model):
	text = models.TextField(max_length=100)
	dataCreacio = models.DateTimeField()
	dataModificacio = models.DateTimeField()
	usuari = models.ForeignKey(Usuari)
	item = models.ForeignKey(Item)

class Idioma(models.Model):
	nom = models.TextField(max_length=30)
	imatge = models.TextField(max_length=30)


class Tag(models.Model):
	nom = models.TextField(max_length=100)

class Categoria_aux(models.Model):
	categoria = models.ForeignKey(Categoria)
	item = models.ForeignKey(Item)

class Tags_aux(models.Model):
	item = models.ForeignKey(Item)
	tag = models.ForeignKey(Tag)

class Idioma_aux(models.Model):
	item = models.ForeignKey(Item)
	idioma = models.ForeignKey(Idioma)

class Comentaris_aux(models.Model):
	comentari= models.ForeignKey(Comentari,related_name="comentari_principal")
	resposta= models.ForeignKey(Comentari,related_name="comentari_secundari")

class Seccio_aux(models.Model):
	seccio = models.ForeignKey(Seccio,related_name="seccio_principal")
	subseccio = models.ForeignKey(Seccio,related_name="seccio_secundaria")

class Valoracio(models.Model):
	item = models.ForeignKey(Item,related_name="item_valorat")
	usuari = models.ForeignKey(Usuari)
	nota = models.IntegerField(max_length=2)

