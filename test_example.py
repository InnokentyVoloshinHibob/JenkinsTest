from seleniumbase import BaseCase


class Example(BaseCase):

    @staticmethod
    def test_example1():
        if 2+2 != 4:
            assert False

    @staticmethod
    def test_example2():
        if 2 * 2 != 4:
            assert False

    @staticmethod
    def test_example3():
        if 2 / 2 != 4:
            assert False
