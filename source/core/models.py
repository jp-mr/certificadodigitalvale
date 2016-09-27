from django.db import models
from django.conf import settings

def upload_location(instance, filename):
    return '%s/produtos/%s' % (settings.MEDIA_ROOT, filename)

class Produto(models.Model):
    imagem = models.ImageField(upload_to=upload_location, blank=True, null=True)
    certificado = models.CharField(max_length=80)
    modelo = models.CharField(max_length=80)
    bloco_vemelho_validade = models.CharField(max_length=80, blank=True)
    bloco_vermelho_preço = models.CharField(max_length=80, blank=True)
    bloco_verde_validade = models.CharField(max_length=80, blank=True)
    bloco_verde_preço = models.CharField(max_length=80, blank=True)
    bloco_azul_validade = models.CharField(max_length=80, blank=True)
    bloco_azul_preço = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return self.certificado

