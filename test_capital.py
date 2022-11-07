import pytest

def capital_case(x):
    if not isinstance(x, str):
        raise TypeError('Should be a string')
    return x.capitalize()

@pytest.fixture
def output_value():
    return 'Paula'

def test_capital_case(output_value):
    assert capital_case('paula') == output_value
    
def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(8)