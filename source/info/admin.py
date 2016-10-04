from django.contrib import admin

from .forms import EcnpjForm, EcpfForm, NFeForm
from .models import Ecnpj, Ecpf, NFe


class EcnpjModelAdmin(admin.ModelAdmin):
    form = EcnpjForm


class EcpfModelAdmin(admin.ModelAdmin):
    form = EcpfForm


class NFeModelAdmin(admin.ModelAdmin):
    form = NFeForm


admin.site.register(Ecnpj, EcnpjModelAdmin)
admin.site.register(Ecpf, EcpfModelAdmin)
admin.site.register(NFe, NFeModelAdmin)
