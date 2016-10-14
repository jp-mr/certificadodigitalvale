from django import forms


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
