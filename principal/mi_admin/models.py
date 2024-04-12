from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    correo = models.EmailField()
    rol = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    # ... otros campos y métodos

    class Meta:
        app_label = 'mi_admin'

class Puerta(models.Model):
    nombre = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    fecha_instalacion = models.DateField()
    descripcion = models.TextField(blank=True, null=True)
    # ... otros campos y métodos

    class Meta:
        app_label = 'mi_admin'

class Actividad(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    puerta = models.ForeignKey(Puerta, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    accion = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)
    exito = models.BooleanField()
    # ... otros campos y métodos

    class Meta:
        app_label = 'mi_admin'

