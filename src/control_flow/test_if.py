"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """IF statement"""

    number = 15
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    else:
        conclusion = 'Number bigger than or equal to one'

    assert conclusion == 'Number bigger than or equal to one'


def test_nested_if_statement():
    """Nested IF statement"""

    age = 20
    has_license = True
    conclusion = ''

    if age >= 18:
        if has_license:
            conclusion = 'Can drive'
        else:
            conclusion = 'No license'
    else:
        conclusion = 'Too young'

    assert conclusion == 'Can drive'

def test_multiple_elif_statements():
    """Multiple ELIF statements"""

    grade = 85
    conclusion = ''

    if grade >= 90:
        conclusion = 'A'
    elif grade >= 80:
        conclusion = 'B'
    elif grade >= 70:
        conclusion = 'C'
    elif grade >= 60:
        conclusion = 'D'
    else:
        conclusion = 'F'

    assert conclusion == 'B'