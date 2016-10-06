from django.contrib import admin

from .forms import EcnpjForm, EcpfForm, NFeForm
from .models import Ecnpj, Ecpf, NFe


class EcnpjModelAdmin(admin.ModelAdmin):
    form = EcnpjForm
    actions = ['delete_selected']


class EcpfModelAdmin(admin.ModelAdmin):
    form = EcpfForm
    actions = ['delete_selected']


class NFeModelAdmin(admin.ModelAdmin):
    form = NFeForm
    actions = ['delete_selected']


admin.site.register(Ecnpj, EcnpjModelAdmin)
admin.site.register(Ecpf, EcpfModelAdmin)
admin.site.register(NFe, NFeModelAdmin)
