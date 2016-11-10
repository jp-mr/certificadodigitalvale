from django.test import TestCase

from model_mommy import mommy

from info.models import Ecnpj, Ecpf, NFe


class InfoTest(TestCase):

    models = [Ecnpj, Ecpf, NFe]

    def create_objects(self, *args, **kwargs):
        objects = []
        for model in self.models:
            obj = mommy.make(model)
            objects.append(obj)
        return objects

    def test_info_creation(self):
        objects = self.create_objects()
        for num, obj in enumerate(objects):
            self.assertTrue(isinstance(obj, self.models[num]))
            self.assertEqual(obj.__str__(), obj.título)
            self.assertEqual(
                obj.get_markdown(),
                "<p>" + obj.descrição  + "</p>\n"
                )
