from django.db import models
from django.utils.safestring import mark_safe

from markdown_deux import markdown


class Info(models.Model):

    título = models.CharField(max_length=80)
    descrição = models.TextField()

    def __str__(self):
        return self.título

    def get_markdown(self):
        descrição = self.descrição
        markdown_text = markdown(descrição)
        return mark_safe(markdown_text)

    class Meta:
        abstract = True


class Ecnpj(Info):

    class Meta:
        verbose_name_plural = "e-CNPJ"
        ordering = ['id']


class Ecpf(Info):

    class Meta:
        verbose_name_plural = "e-CPF"
        ordering = ['id']


class NFe(Info):

    class Meta:
        verbose_name_plural = "NF-e"
        ordering = ['id']
