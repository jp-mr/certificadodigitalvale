import pytest
from model_mommy import mommy

from cs_modal.models import CreditServiceModal


@pytest.mark.django_db
def test_credit_service_modal_creation():
    cs = mommy.make(CreditServiceModal)
    assert isinstance(cs, CreditServiceModal) == True
    assert cs.__str__() ==  cs.serviço
    assert cs.get_markdown() == "<p>" + cs.descrição + "</p>\n"
