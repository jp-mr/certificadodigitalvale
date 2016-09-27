from django.contrib import admin
from django.contrib.admin.sites import AdminSite

from .models import Produto


AdminSite.site_header = "Certificado Digital Vale"
AdminSite.site_title = "Certificado Digital Vale"


class ProdutoModelAdmin(admin.ModelAdmin):

    list_display = ['certificado', 'modelo',]
    #readonly_fields = ['download', ]
    list_filter = ['certificado', 'modelo']
    search_fields = ['certificado', 'modelo']

    class Meta:
        model = Produto


admin.site.register(Produto, ProdutoModelAdmin)
