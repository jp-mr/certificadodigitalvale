from django import forms
from pagedown.widgets import AdminPagedownWidget

from .models import CreditServiceModal


class CreditServiceModalForm(forms.ModelForm):

    descrição = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = CreditServiceModal
        fields = [
            'título',
            'descrição',
            'name_id',
            'serviço'
            ]
