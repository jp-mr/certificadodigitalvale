from django.conf.urls import url

from .views import (
            home,
            ecnpj,
            ecpf,
            nfe,
        )


urlpatterns = [

    url(r'^$', home, name='home'),
    url(r'^e-cnpj$', ecnpj, name='ecnpj'),
    url(r'^e-cpf$', ecpf, name='ecpf'),
    url(r'^nf-e$', nfe, name='nfe'),
]
