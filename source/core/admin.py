from django.contrib import admin
from django.contrib.admin.sites import AdminSite

from .models import Ecnpj, Ecpf, NFe


AdminSite.site_header = "Certificado Digital Vale"
AdminSite.site_title = "Certificado Digital Vale"


class ProdutoModelAdmin(admin.ModelAdmin):

    list_display = ['modelo', 'posição']
    # list_filter = ['modelo']
    # search_fields = ['modelo']


class EcnpjModelAdmin(ProdutoModelAdmin):

    class Meta:
        model = Ecnpj


class EcpfModelAdmin(ProdutoModelAdmin):

    class Meta:
        model = Ecpf


class NFeModelAdmin(ProdutoModelAdmin):

    class Meta:
        model = NFe


admin.site.register(Ecnpj, EcnpjModelAdmin)
admin.site.register(Ecpf, EcpfModelAdmin)
admin.site.register(NFe, NFeModelAdmin)
