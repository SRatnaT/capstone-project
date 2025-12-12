import pytest


class TestSample:

    def inc(self, x):
        return x + 1

    def dec(self, x):
        return x - 1

    def test_inc(self):

        assert self.inc(4) == 5

    def test_dec(self):

        assert self.dec(4) == 3


class TestDemoSample:

    value = 1

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):

        assert self.value == 1


class TestParameterize:

    @pytest.mark.parametrize("a , b , expected", [(1, 2, 3), (5, 7, 12)])
    def test_add(self, a, b, expected):

        assert a + b == expected


# Testing pytest.approx


def test_floating():

    assert (0.1 + 0.2) == pytest.approx(0.3)
