from django.conf import settings
from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase

from django import forms


from core.forms import ContactForm
from core.views import home

class CoreTest(TestCase):

    def setUp(self):
        self.valid_post_email = {
                'nome': 'Michel Rodrigues',
                'email': 'email@teste.com',
                'assunto': 'TESTE',
                'mensagem': '1, 2... TESTANDO!',
                }

    def test_view_home(self):
        response = self.client.get(reverse('core:home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'forms.html')
        self.assertTemplateUsed(response, 'home/home.html')
        self.assertTemplateUsed(
                response,
                'service-credit-modal/credit-service-modal.html'
                )

    def test_has_form_on_context(self):
        response = self.client.get(reverse('core:home'))
        self.assertIsInstance(response.context['form'], ContactForm)
        self.assertTemplateUsed(response, 'forms.html')

    def test_contact_email_field_pattern(self):
        self.assertFieldOutput(
                forms.EmailField,
                {'a@a.com': 'a@a.com'},
                {'aaa': ['Informe um endereço de email válido.']}
                )

    def test_send_contact_email(self):
        self.assertEquals(len(mail.outbox), 0)
        response = self.client.post(reverse('core:home'), self.valid_post_email)
        self.assertEqual(response.status_code, 302)
        self.assertEquals(len(mail.outbox), 1)

    def test_content_contact_email(self):
        response = self.client.post(reverse('core:home'), self.valid_post_email)
        email = mail.outbox[0]
        print(email)
        self.assertEqual(email.from_email, 'certificadodigitalvale@gmail.com')
        self.assertEqual(email.subject, 'TESTE')
        self.assertEqual(
                email.body,
                'Michel Rodrigues <email@teste.com> \n\n 1, 2... TESTANDO!')
        self.assertEqual(email.to, ['certificadodigitalvale@gmail.com'])
        self.assertEqual(email.reply_to, ['email@teste.com'])
