from src.simple_library_01.functions import get_month_days
import unittest


class MyTestCase(unittest.TestCase):

    def test_get_month_days(self):
        with self.assertRaises(AttributeError):
            get_month_days(2000, 13)


if __name__ == '__main__':
    unittest.main()

def test_month_30():
    assert 30 == get_month_days(1930, 1)

def test_month_29():
    assert 29 == get_month_days(1588, 2)

def test_month_28():
    assert 28 == get_month_days(1587, 2)

def test_month_4():
    for m in [4, 6, 9, 11]:
        assert 30 == get_month_days(1587, m)

def test_month_21():
    assert 31 == get_month_days(1587, 3)

