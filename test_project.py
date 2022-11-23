from project import get_os, compute_distance, get_aps
from pytest import raises

def test_get_os():
    assert get_os() in ['linux', 'win32', 'mac']  
    assert get_os() != "windows"


def test_compute_distance():
    assert compute_distance(-64) ==  7.041434423635424
    with raises(ValueError):
        compute_distance(1)
        compute_distance(9)
        compute_distance('ola')


def test_get_aps():
    with raises(NotImplementedError):
        get_aps('linux3')
        get_aps('linux5')