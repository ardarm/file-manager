#!/usr/bin/env python3

import pytest

from src.operations import _read_file, _create_file, _copy_file, _move_file, _remove_file


@pytest.fixture
def file_(tmp_path):
    test_file = tmp_path / 'file1.txt'
    with open(test_file, "w") as f:
        f.write("hello world\n")
    return test_file


@pytest.fixture
def directory_(tmpdir):
    first_directory = tmpdir.mkdir("test")
    second_directory = tmpdir.mkdir("test2")
    return (first_directory, second_directory)


def test_read_file_success(file_, capfd):
    _read_file(file_)
    assert capfd.readouterr().out.strip() == "hello world"


def test_read_file_not_found(file_, capfd):
    _read_file(f"{file_}2")
    assert capfd.readouterr().out.strip() == f"{file_}2 doesn't exist!"


def test_read_file_that_is_directory(directory_, capfd):
    _read_file(directory_[0])
    assert capfd.readouterr().out.strip(
    ) == f"{directory_[0]} is a directory, cannot be read!"


def test_create_file_success(file_, capfd):
    _create_file(f"{file_}2")
    assert capfd.readouterr().out.strip() == f"{file_}2 created"


def test_create_file_already_exist(file_, capfd):
    _create_file(file_)
    assert capfd.readouterr().out.strip() == f"{file_} already exist!"


def test_copy_file_success(file_, capfd):
    _copy_file(file_, f"{file_}3.txt")
    assert capfd.readouterr().out.strip() == f"{file_} copied to {file_}3.txt"


def test_copy_file_already_exist(file_, capfd):
    _copy_file(file_, file_)
    assert capfd.readouterr().out.strip() == f"{file_} already exist!"


def test_copy_file_doesnt_exist(file_, capfd):
    _copy_file("file4.txt", "file5.txt")
    assert capfd.readouterr().out.strip() == "file4.txt doesn't exist"


def test_copy_file_that_is_directory(directory_, capfd):
    _copy_file(directory_[0], directory_[1])
    assert capfd.readouterr().out.strip(
    ) == f"{directory_[0]} is a directory, feature will be added soon!"


def test_move_file_success(file_, directory_, capfd):
    _move_file(file_, directory_[0])
    assert capfd.readouterr().out.strip(
    ) == f"{file_} moved to {directory_[0]}"


def test_move_file_doesnt_exist(file_, directory_, capfd):
    _move_file(f"{file_}3", directory_[0])
    assert capfd.readouterr().out.strip() == f"{file_}3 doesn't exist!"


def test_remove_file_success(file_, capfd):
    _remove_file(file_)
    assert capfd.readouterr().out.strip() == f"{file_} removed!"


def test_remove_file_doesnt_exist(file_, capfd):
    _remove_file(f"{file_}3")
    assert capfd.readouterr().out.strip() == f"{file_}3 doesn't exist!"
