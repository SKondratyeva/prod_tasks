from src.simple_library_01.functions import  add, is_leap
import pytest

def test_sum_positive():
    assert 7 == add( 3, 4)

def test_sum_positive2():
    assert 7 == add( 4,  3)

def test_sum_negative():
    assert -7 == add( -4,  -3)

def test_sum_negative2():
    assert -7 == add( -3,  -4)

def test_sum_zero():
    assert 3 == add( 3, 0)

def test_floats():
    assert 1.2 == add(1.2, 0)

def test_floats2():
    assert 2.9 == add(1.2, 1.7)


