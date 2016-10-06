from django.contrib import admin

from .forms import CreditServiceModalForm
from .models import CreditServiceModal


class CreditServiceModalAdmin(admin.ModelAdmin):
    form = CreditServiceModalForm

    # list_display = ['título', 'id', 'name_id', 'serviço']

    # Não permite a adição de novos objetos no admin
    def has_add_permission(self, request):
        return False

    # Não permite a remoção de objetos no admin
    def has_delete_permission(self, request, obj=CreditServiceModal):
        return False



admin.site.register(CreditServiceModal, CreditServiceModalAdmin)
