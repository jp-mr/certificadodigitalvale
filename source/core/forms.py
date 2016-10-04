from django import forms
# from pagedown.widgets import AdminPagedownWidget

# from .models import InfoCNPJ


class ContactForm(forms.Form):
    nome = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Digite seu nome completo'
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'Digite seu endereço de email'
    }))
    assunto = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Digite o assunto da mensagem'
    }))
    mensagem = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Digite o assunto da mensagem'
    }))


# class InfoCNPJForm(forms.ModelForm):
#     descrição = forms.CharField(widget=AdminPagedownWidget())

#     class Meta:
#         model = InfoCNPJ
#         fields = "__all__"
