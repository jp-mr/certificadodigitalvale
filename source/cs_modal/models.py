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
        #ordering = ['posição']

    def __str__(self):
        # Se o objeto não estiver sendo exibido no admin, substitua pelo
        # atributo '.título'
        return self.serviço

    def get_markdown(self):
        descrição = self.descrição
        markdown_text = markdown(descrição)
        return mark_safe(markdown_text)



# def pre_save_cs_modal_receiver(sender, instance, *args, **kwargs):
# 
#    """
#     TODO: Comentar | descomentar pre_save topo e rodapé
#    """
#
#     modal_attr = [
#         ['analise','Análise de Crédito'],
#         ['consulta','Consulta de CPF/CNPJ'],
#         ['infobusca','InfoBusca'],
#         ['meproteja','MeProteja'],
#         ['negativacao','Negativação de devedores'],
#     ]
# 
#     qs = CreditServiceModal.objects.first()
#
#     obj_id = instance.id - qs.id
#     instance.name_id = modal_attr[obj_id][0]
#     instance.serviço = modal_attr[obj_id][1]
# 
# 
# pre_save.connect(pre_save_cs_modal_receiver, sender=CreditServiceModal)
