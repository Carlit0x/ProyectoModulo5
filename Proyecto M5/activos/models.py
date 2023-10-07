from django.db import models

class Grupo(models.Model):
    #id_grupo = models.PositiveIntegerField()
    grupo_contab = models.CharField(max_length=50, unique=True)
    partida = models.PositiveIntegerField()
    def __str__(self):
        return '%s (%s)' % (self.grupo_contab, self.partida)

class Activo(models.Model):
	#id_bien = models.PositiveIntegerField()
	bien = models.CharField(max_length=50, unique=True)
	grupo_contab = models.ForeignKey(Grupo, on_delete=models.CASCADE)
	descripcion = models.CharField(max_length=150, unique=True)
	codigo = models.CharField(max_length=20, unique=True)
	fecha = models.DateField()
	estado = models.CharField(max_length=20, unique=False)
	def __str__(self):
		return self.bien
      
class Personal(models.Model):
	ci = models.PositiveIntegerField()
	nombres = models.CharField(max_length=30, unique=True)
	apellidos = models.CharField(max_length=30, unique=True)
	cargo = models.CharField(max_length=30, unique=True)
	seccion = models.CharField(max_length=20, unique=True)

class Asignar(models.Model):
	fecha = models.DateField()
	ci_persona = models.ManyToManyField(Personal)
	bien_activo = models.ManyToManyField(Activo)
	#id_bien = models.PositiveIntegerField()