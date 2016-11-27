from django.conf import settings
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.utils.cache import patch_response_headers

from .forms import ContactForm
from cs_modal.models import CreditServiceModal
from info.models import (
        Ecnpj as InfoEcnpj,
        Ecpf as InfoEcpf,
        NFe as InfoNFe,
        )
from tabela.models import (
        Ecnpj as TabelaEcnpj,
        Ecpf as TabelaEcpf,
        NFe as TabelaNFe,
        )
from tabela.utilities import table


def home(request):

    if request.method == 'POST':

        form = ContactForm(request.POST or None)

        if form.is_valid():

            name = form.cleaned_data.get('nome')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('assunto')
            message = form.cleaned_data.get('mensagem')
            from_email = 'certificadodigitalvale@gmail.com' # "%s <%s>" % (name, email) # RFC 5322
            to_email = ['certificadodigitalvale@gmail.com', ]
            reply_to = [email,]

            if settings.EMAIL_DESTINY:
                to_email += [settings.EMAIL_DESTINY]

            contact_message = "%s <%s> \n\n %s" % (name, email, message)

            msg = EmailMessage(
                    subject=subject,
                    body=contact_message,
                    to=to_email,
                    from_email=from_email,
                    reply_to=reply_to,
                    )

            msg.send(fail_silently=False)

            return redirect(reverse('core:home') + '?sent=True')

    form = ContactForm()

    cs_modals = CreditServiceModal.objects.all()

    template = 'home/home.html'
    context = {
        'form': form,
        'cs_modals': cs_modals,
        'home':'home'
    }

    msg_sent = request.GET.get('sent', False)
    if msg_sent:
        context['message_sent'] = 'message_sent'

    response = render(request, template, context)
    patch_response_headers(response, cache_timeout=7884000)
    return response


def ecnpj(request):

    produtos = table(TabelaEcnpj)

    infos = InfoEcnpj.objects.all()

    template = 'certificado-digital/e-cnpj.html'
    context = {
            'produtos': produtos,
            'certificado': 'e-cnpj',
            'saiba_mais_produto': 'e-CNPJ',
            'Infos': infos,
            }

    response = render(request, template, context)
    patch_response_headers(response, cache_timeout=7884000)
    return response


def ecpf(request):

    produtos = table(TabelaEcpf)

    infos = InfoEcpf.objects.all()

    template = 'certificado-digital/e-cpf.html'
    context = {
            'produtos': produtos,
            'certificado': 'e-cpf',
            'saiba_mais_produto': 'e-CPF',
            'Infos': infos,
            }

    response = render(request, template, context)
    patch_response_headers(response, cache_timeout=7884000)
    return response


def nfe(request):

    produtos, tabela_nfe = table(TabelaNFe)

    infos = InfoNFe.objects.all()

    template = 'certificado-digital/nf-e.html'
    context = {
            'produtos': produtos,
            'certificado': 'nf-e',
            'saiba_mais_produto': 'NF-e',
            'tabela_nfe': tabela_nfe,
            'Infos': infos,
            }

    response = render(request, template, context)
    patch_response_headers(response, cache_timeout=7884000)
    return response
