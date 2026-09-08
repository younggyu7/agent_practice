from .calculator import add, substract


def test_add():
    result = add(10, 20)
    assert result == 30  # 검사 명령어


def test_substract():
    result = substract(10, 3)
    assert result == 7
