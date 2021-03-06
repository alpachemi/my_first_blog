from django.db import models
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey('auth.User',
		 					on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title

class Usuario(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Id para un usuario")
    #nombre = models.ForeignKey('Nombre', on_delete=models.SET_NULL, null=True) 
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
	fecha_nacimiento = models.DateTimeField(blank=True, null=False)
    telefono_1 = models.CharField(max_length=15)
    telefono_2 = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
	provincia = models.CharField(max_length=40)
	localidad = models.CharField(max_length=40)
	direccion = models.CharField(max_length=100)
	codigo_postal = models.CharField(max_length=10)
	sexo = models.CharField(max_length=1)
	carne_conducir = models.BooleanField(default=False)
	cuidador = models.BooleanField(default=False)
	administrador = models.BooleanField(default=False)
	
    #LOAN_STATUS = (
    #    ('m', 'Maintenance'),
    #    ('o', 'On loan'),
    #    ('a', 'Available'),
    #    ('r', 'Reserved'),
    #)

    def __str__(self):
        return '%s (%s)' % (self.id,self.Usuario.id)
		
    def publish(self):
		self.save()
	