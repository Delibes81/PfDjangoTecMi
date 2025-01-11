from django.db import models

# Create your models here.

class TBL_Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    id_nomina = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return f"{self.id_nomina}, {self.nombre}"

class TBL_Video(models.Model):
    id_video = models.AutoField(primary_key=True)
    nombre_video = models.CharField(max_length=50)
    extension_video = models.CharField(max_length=5)
    tamano_video = models.IntegerField()

    def __str__(self):
        return f"{self.id_video}, {self.nombre_video}"

class TBL_VideoUsuario(models.Model):
    id_usuario = models.ForeignKey(TBL_Usuario, on_delete=models.CASCADE)
    id_video = models.ForeignKey(TBL_Video, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_usuario}, {self.id_video}"