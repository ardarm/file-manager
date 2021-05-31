import pytest

from src.operations import _read_file


@pytest.fixture
def file_(tmp_path):
    test_file = tmp_path / 'file1.txt'
    with open(test_file, "w") as f:
        f.write("hello world\n")
    return test_file


def test_read_file_success(file_, capfd):
    _read_file(file_)
    assert capfd.readouterr().out.strip() == "hello world"


def test_read_file_not_found():
    pass


def test_read_file_that_is_directory():
    pass
