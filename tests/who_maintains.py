import pytest
from pypi_examiner import examiner


def test_package_exists():
    pypi = examiner()
    result = pypi.who_maintains("unishox2_py3")

    assert result == ["tweedge"]


def test_package_does_not_exist():
    pypi = examiner()
    result = pypi.who_maintains("httpxfaster")

    assert result == []


def test_multiple_maintainers():
    pypi = examiner()
    result = pypi.who_maintains("boto")

    assert "aws" in result and "garnaat" in result
