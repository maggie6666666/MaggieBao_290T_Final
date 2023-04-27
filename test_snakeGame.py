from snakeGame import capital_case
from snakeGame import square


def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

def test_square():
    assert square(5) == 25