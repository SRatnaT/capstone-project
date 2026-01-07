import os

import pytest


class Fruit:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):

        return self.name == other.name


@pytest.fixture
def my_fruit():
    return Fruit("orange")


@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]


def test_my_fruit_in_fruit_basket(my_fruit, fruit_basket):

    assert my_fruit in fruit_basket


class TestFixture:

    @pytest.fixture
    def sample_number(self):
        return 5

    def test_increment(self, sample_number):

        assert sample_number + 1 == 6

    def test_decrement(self, sample_number):

        assert sample_number - 1 == 4


# Built in tmp_path fixture


class TestFiles:

    def test_write_files(self, tmp_path):

        file_path = tmp_path / "example.txt"
        file_path.write_text("MESSI IS THE GOAT")

        content = file_path.read_text()
        assert content == "MESSI IS THE GOAT"

    def test_multiple_files(self, tmp_path):

        file_1 = tmp_path / "file1.txt"
        file_2 = tmp_path / "file2.txt"

        file_1.write_text("FILE 1")
        file_2.write_text("FILE 2")

        files = list(tmp_path.iterdir())
        assert len(files) == 2


class TestMonkeyPatch:

    def test_env(self, monkeypatch):

        api_key = os.environ.get("API_KEY")
        print(api_key)

        monkeypatch.setenv("API_KEY", "12345")
        assert os.environ["API_KEY"] == "12345"


# Fixture scopes


@pytest.fixture(scope="function")
def my_fixture_1():

    return []


def test_function_scope_a(my_fixture_1):

    my_fixture_1.append(1)

    assert my_fixture_1 == [1]


def test_function_scope_b(my_fixture_1):

    assert my_fixture_1 == []


@pytest.fixture(scope="class")
def my_fixture_class():

    return []


class TestFixtureClass:

    def test_class_scope_a(self, my_fixture_class):

        my_fixture_class.append(1)

        assert my_fixture_class == [1]

    def test_class_scope_b(self, my_fixture_class):

        my_fixture_class.append(2)

        assert my_fixture_class == [1, 2]


@pytest.fixture(scope="module")
def my_fixture_module():

    return []


def test_fixture_module_a(my_fixture_module):

    my_fixture_module.append(3)

    assert my_fixture_module == [3]


def test_fixture_module_b(my_fixture_module):

    my_fixture_module.append(4)

    assert my_fixture_module == [3, 4]
