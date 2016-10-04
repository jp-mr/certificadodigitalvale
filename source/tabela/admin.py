from django.contrib import admin

from .models import Ecnpj, Ecpf, NFe


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
