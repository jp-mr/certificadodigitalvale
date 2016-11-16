from django import forms
from pagedown.widgets import AdminPagedownWidget

from .models import Ecnpj, Ecpf, NFe


class EcnpjForm(forms.ModelForm):
    descrição = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Ecnpj
        fields = ['título', 'descrição']


class EcpfForm(forms.ModelForm):
    descrição = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Ecpf
        fields = ['título', 'descrição']


class NFeForm(forms.ModelForm):
    descrição = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = NFe
        fields = ['título', 'descrição']
