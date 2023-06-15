import pytest
from module import calculator
def test_calculate():
    result = calculator.calculate(2, 3)
    assert result == -1


if __name__ == '__main__':
    pytest.main()
