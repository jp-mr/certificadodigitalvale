# from django.core.files.uploadedfile import SimpleUploadedFile
import pytest

from model_mommy import mommy

from tabela.models import Ecnpj, Ecpf, NFe


models = [Ecnpj, Ecpf, NFe]


def create_objects():
    objects = []
    for model in models:
        obj = mommy.make(model)
        objects.append(obj)
    return objects


@pytest.mark.django_db
def test_produto_creation():
    objects = create_objects()
    for num, obj in enumerate(objects):
        assert isinstance(obj, models[num]) == True
        assert obj.__str__() == obj.certificado
