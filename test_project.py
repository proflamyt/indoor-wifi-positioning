from project import get_os

def test_get_os():
    assert get_os() in ['linux', 'win32', 'mac']  


def test_function_2():
    ...


def test_function_n():
    ...