from django import forms
from crispy_forms.helper import FormHelper
import re

class ContactForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.fields['nome'].widget.attrs = {
                'placeholder': 'Digite seu nome completo',
                'oninvalid': "this.setCustomValidity('Por favor, preencha o campo com o seu nome')",
                'oninput':"setCustomValidity('')",
                }
        self.fields['email'].widget.attrs = {
                'placeholder': 'Digite seu endereço de email',
                'pattern': "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{1,6})",
                'oninvalid': "setCustomValidity('Por favor, preencha o campo com um endereço de email válido')",
                'oninput': "InvalidMsg(this)"
                }
        self.fields['assunto'].widget.attrs = {
                'placeholder': 'Digite o assunto da mensagem',
                'oninvalid': "this.setCustomValidity('Por favor, preencha o campo com o assunto da mensagem')",
                'oninput':"setCustomValidity('')",
                }
        self.fields['mensagem'].widget.attrs = {
                'placeholder': 'Digite sua mensagem',
                'oninvalid': "this.setCustomValidity('Por favor, preencha o campo com a sua mensagem')",
                'oninput':"setCustomValidity('')",
                }

    nome = forms.CharField()
    email = forms.EmailField()
    assunto = forms.CharField()
    mensagem = forms.CharField(widget=forms.Textarea)

    # def clean_email(self):

    #     email = self.cleaned_data.get('email')
    #     rgx = re.findall(
    #             r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{1,6})',
    #             email
    #             )
    #     if rgx:
    #         print(rgx)
    #     if not rgx:
    #         raise forms.ValidationError("Entre com um endereço de email válido")
    #     return email
