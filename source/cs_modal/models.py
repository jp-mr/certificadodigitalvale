from django.db import models
# from django.db.models.signals import pre_save
from django.utils.safestring import mark_safe

from markdown_deux import markdown


class CreditServiceModal(models.Model):
    título = models.CharField(max_length=80)
    descrição = models.TextField()
    name_id = models.CharField(max_length=50)
    serviço = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Credit Service Modal"

    def __str__(self):
        return self.serviço

    def get_markdown(self):
        descrição = self.descrição
        markdown_text = markdown(descrição)
        return mark_safe(markdown_text)
