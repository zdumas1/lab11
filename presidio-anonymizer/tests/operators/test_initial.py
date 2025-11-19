import pytest
from presidio_anonymizer.operators import Initial

@pytest.mark.parametrize(
    "input_text, initials",
    [
        ("John Smith", "J. S."),
    ],
)
def test_given_value_for_initial(input_text, initials):
    text = Initial().operate(input_text) == initials
    assert text == initials
def test_correct_name():
    assert Initial().operator_name() == "initial"
def test_initial_trims_whitespace():
    operator = Initial()
    result = operator.anonymize("     Eastern    Michigan   University ")
    assert result == "E. M. U."