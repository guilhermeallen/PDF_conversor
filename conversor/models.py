from django.db import models

# Create your models here.
class Arquivo(models.Model):
    arquivo = models.FileField(upload_to='uploads/')
    convertido_em = models.DateTimeField(auto_now_add=True)
