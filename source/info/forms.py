from django import forms
from pagedown.widgets import AdminPagedownWidget

from .models import Ecnpj, Ecpf, NFe


class EcnpjForm(forms.ModelForm):
    descrição = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Ecnpj
        fields = "__all__"


class EcpfForm(forms.ModelForm):
    descrição = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Ecpf
        fields = "__all__"


class NFeForm(forms.ModelForm):
    descrição = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = NFe
        fields = "__all__"
