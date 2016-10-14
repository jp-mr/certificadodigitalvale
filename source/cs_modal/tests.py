from django.test import TestCase

from model_mommy import mommy

from .models import CreditServiceModal


class CreditServiceModalTest(TestCase):

    def test_credit_service_modal_creation(self):
        cs = mommy.make(CreditServiceModal)
        self.assertTrue(isinstance(cs, CreditServiceModal))
        self.assertEqual(cs.__str__(), cs.serviço)
        self.assertEqual(
                cs.get_markdown(),
                "<p>" + cs.descrição + "</p>\n"
                )
