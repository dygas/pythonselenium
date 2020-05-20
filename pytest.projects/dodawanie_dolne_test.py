import pytest
@pytest.mark.parametrize('skladnik,suma',[(5,10),(2,4)])
def test_dodawania(skladnik,suma):
    assert skladnik + skladnik == suma


# @pytest.mark.skip piszemy przy kazdej metodzie na poczatku wtedy omijamy
#@pytest.mark.xfail TAKA BEDZIE KONCZYLA SIE NIEPOWODZENIEM
