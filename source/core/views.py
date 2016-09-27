from django.conf import settings
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from .forms import ContactForm


def home(request):

    if request.method == 'POST':

        form = ContactForm(request.POST or None)

        if form.is_valid():

            name = form.cleaned_data.get('nome')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('assunto')
            message = form.cleaned_data.get('mensagem')
            from_email = "%s <%s>" % (name, email) # RFC 5322
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

    template = 'home/home.html'
    context = {
        'form': form,
    }

    msg_sent = request.GET.get('sent', False)
    if msg_sent:
        context['message_sent'] = 'message_sent'

    return render(request, template, context)


def ecnpj(request):

    template = 'certificado-digital/e-cnpj.html'
    context = {}

    return render(request, template, context)


def ecpf(request):

    template = 'certificado-digital/e-cpf.html'
    context = {}

    return render(request, template, context)


def nfe(request):

    template = 'certificado-digital/nf-e.html'
    context = {}

    return render(request, template, context)
