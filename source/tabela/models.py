from django.db import models


def upload_location(instance, filename):
    return 'produtos/%s/%s' % (instance, filename)


class Produto(models.Model):
    imagem = models.ImageField(
            upload_to=upload_location,
            blank=True,
            null=True,
            )
    modelo = models.CharField(max_length=80)
    bloco_vermelho_validade = models.CharField(max_length=80, blank=True)
    bloco_vermelho_preço = models.CharField(max_length=80, blank=True)
    bloco_verde_validade = models.CharField(max_length=80, blank=True)
    bloco_verde_preço = models.CharField(max_length=80, blank=True)
    bloco_azul_validade = models.CharField(max_length=80, blank=True)
    bloco_azul_preço = models.CharField(max_length=80, blank=True)
    posição = models.PositiveSmallIntegerField(unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.certificado


class Ecnpj(Produto):

    certificado = "e-CNPJ"

    class Meta:
        verbose_name_plural = "e-CNPJ"
        ordering = ['posição']


class Ecpf(Produto):

    certificado = "e-CPF"

    class Meta:
        verbose_name_plural = "e-CPF"
        ordering = ['posição']


class NFe(Produto):

    certificado = "PJ NF-e"

    class Meta:
        verbose_name_plural = "NF-e"
        ordering = ['posição']
