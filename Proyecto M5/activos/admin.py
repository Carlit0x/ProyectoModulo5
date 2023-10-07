from django.contrib import admin
from .models import Grupo
from .models import Personal
from .models import Activo
from .models import Asignar

class GrupoAdmin(admin.ModelAdmin):
    list_display = ('grupo_contab', 'partida')
    ordering = ['grupo_contab']
    search_fields = ['partida']

admin.site.register(Grupo,GrupoAdmin)

class ActivoAdmin(admin.ModelAdmin):
    list_display = ('bien', 'descripcion', 'codigo', 'estado', 'fecha')
    ordering = ['fecha']
admin.site.register(Activo, ActivoAdmin)

admin.site.register(Personal)

admin.site.register(Asignar)