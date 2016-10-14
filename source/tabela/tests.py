# from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from model_mommy import mommy

from .models import Ecnpj, Ecpf, NFe


class ProdutoTest(TestCase):

    models = [Ecnpj, Ecpf, NFe]

    def create_objects(self, *args, **kwargs):
        objects = []
        for model in self.models:
            obj = mommy.make(model)
            objects.append(obj)
        return objects

    def test_produto_creation(self):
        objects = self.create_objects()
        for num, obj in enumerate(objects):
            self.assertTrue(isinstance(obj, self.models[num]))
            self.assertEqual(obj.__str__(), obj.certificado)
