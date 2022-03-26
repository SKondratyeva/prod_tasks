import os, sys

parentdir = os.path.dirname('task5/')
sys.path.insert(0, parentdir)
from src.simple_library_01.functions import add, is_leap

def test_add_0():
    assert 7 == add( 3, 4)

def test_add_1():
    assert 7 == add( 4,  3)

def test_add_2():
    assert -7 == add( -4,  -3)

def test_add_3():
    assert -7 == add( -3,  -4)

def test_add_4():
    assert 3 == add( 3, 0)

def test_add_5():
    assert 1.2 == add(1.2, 0)

def test_add_6():
    assert 2.9 == add(1.2, 1.7)


