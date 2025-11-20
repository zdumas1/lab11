import pytest
from presidio_anonymizer.operators import Initial

@pytest.mark.parametrize(
    "input_text, initials",
    [
        ("John Smith", "J. S."),
        ("     Eastern    Michigan   University ", "E. M. U."),
        ("@abc", "@A."),              # Task 7
        ("@843A", "@8."),             # Task 7
        ("--**abc", "--**A."),        # Task 7
    ],
)
def test_given_value_for_initial(input_text, initials):
    operator = Initial()
    result = operator.anonymize(input_text)
    assert result == initials
def test_correct_name():
    assert Initial().operator_name() == "initial"
def test_initial_trims_whitespace():
    operator = Initial()
    result = operator.anonymize("     Eastern    Michigan   University ")
    assert result == "E. M. U."