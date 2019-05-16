from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


class Categoria(models.Model):
	# Sirve para crear categorías de forma dinámica
	nombre = models.CharField(max_length=255, help_text='nombre de la categoria')
	orden = models.PositiveSmallIntegerField(help_text='estable la prioridad con la que se ordena')
	activo = models.BooleanField(default=True)

	def __str__(self):
		return self.nombre


class Novedad(models.Model):
	# Sirve para crear y almacenar novedades
	titulo = models.CharField(
		max_length=255,
		help_text='Ingrese el titulo de la novedad',
		unique=True
	)
	cuerpo = RichTextField()
	activo = models.BooleanField(default=True)
	dueño = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
	creación = models.DateTimeField(auto_now_add=True)
	modificación = models.DateTimeField(auto_now=True)
	slug = models.SlugField(max_length=255, editable=False)
	categoría = models.ForeignKey(Categoria, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = 'novedades'

	def save(self):
		self.slug = slugify(self.titulo)
		super(Novedad, self).save(*args, **kwargs)

	def __str__(self):
		return self.titulo

	def getDueño(self):
		return '%s, %s' % (self.dueño.last_name, self.dueño.first_name)
