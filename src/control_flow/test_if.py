"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """IF statement"""

    def check_number(number):
        if number < 0:
            return 'Number is less than zero'
        elif number == 0:
            return 'Number equals to zero'
        elif number < 1:
            return 'Number is greater than zero but less than one'
        elif number < 10:
            return 'Number is less than 10'
        elif number > 100:
            return 'Number is greater than 100'
        else:
            return 'Number bigger than or equal to one'

    assert check_number(5) == 'Number is less than 10'
    assert check_number(150) == 'Number is greater than 100'
    assert check_number(15) == 'Number bigger than or equal to one'


def test_nested_if_statement():
    """Nested IF statement"""

    def check_driving(age, has_license):
        if age >= 18:
            if has_license:
                return 'Can drive'
            else:
                return 'No license'
        else:
            return 'Too young'

    assert check_driving(20, True) == 'Can drive'
    assert check_driving(20, False) == 'No license'
    assert check_driving(16, True) == 'Too young'

def test_multiple_elif_statements():
    """Multiple ELIF statements"""

    def get_grade(grade):
        if grade >= 90:
            return 'A'
        elif grade >= 80:
            return 'B'
        elif grade >= 70:
            return 'C'
        elif grade >= 60:
            return 'D'
        else:
            return 'F'

    assert get_grade(95) == 'A'
    assert get_grade(85) == 'B'
    assert get_grade(75) == 'C'
    assert get_grade(65) == 'D'
    assert get_grade(55) == 'F'