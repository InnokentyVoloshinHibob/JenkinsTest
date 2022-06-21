from seleniumbase import BaseCase


class Example(BaseCase):

    @staticmethod
    def test_example1():
        assert 2+2 != 4

    @staticmethod
    def test_example2():
        assert 2 * 2 != 4

    @staticmethod
    def test_example3():
        assert 2 / 2 != 1
