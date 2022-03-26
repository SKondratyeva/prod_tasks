from src.simple_library_01.functions import  add, is_leap
import unittest


class MyTestCase(unittest.TestCase):

    def test_is_leap_0(self):
        with self.assertRaises(AttributeError):
            is_leap(-1)


if __name__ == '__main__':
    unittest.main()


def test_is_leap_1():
    assert True == is_leap(32)

def test_is_leap_2():
    assert True == is_leap(16000)

def test_is_leap_3():
    assert False == is_leap(200)

def test_is_leap_4():
    assert True == is_leap(400)

def test_is_leap_5():
    assert False == is_leap(23)
