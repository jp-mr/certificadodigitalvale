# from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from model_mommy import mommy

from tabela.models import Ecnpj, Ecpf, NFe, upload_location


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

    def test_upload_location(self):
        path = upload_location('classe', 'imagem')
        self.assertEqual(path, 'produtos/classe/imagem')
