from django.contrib import admin
from .models import Categoria, Novedad


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'orden')
	search_fields = ['nombre']
	list_filter = ('activo',)


@admin.register(Novedad)
class NovedadAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'cuerpo', 'activo', 'dueño', 'creación', 'modificación', 'slug', 'categoría')
	search_fields = ['titulo', 'dueño', 'categoría']
	list_filter = ('activo',)

	def save_model(self, request, obj, form, change):
		obj.dueño = request.user
		super().save_model(request, obj, form, change)