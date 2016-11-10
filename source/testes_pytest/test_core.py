import pytest
from django.core import mail

from django.shortcuts import resolve_url as r

from core.forms import ContactForm
from core.views import home


"""

client - django.test.Client
An instance of a django.test.Client

def test_view_home(client):
    response = client.get('/')
    assert response.status_code == 200

"""

# rf - RequestFactory
# An instance of a django.test.RequestFactory
def test_view_home(rf):
    request = rf.get('/')
    response = home(request)
    assert response.status_code == 200


@pytest.mark.django_db
def test_view_contact_form(client):
    response = client.post(
                r('core:home'),
                data={
                    'name': 'Nome Completo',
                    'email': 'email@email.com',
                    'subject': 'Assunto do email',
                    'message': 'Mensagem do email',
                })
    assert response.status_code == 200
    assert len(mail.outbox) == 1
    #assert mail.outbox[0].subject == 'Assunto do email'
