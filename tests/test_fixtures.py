import os

import pytest


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
