import pytest
from pypi_examiner import examiner


def test_package_exists():
    pypi = examiner()
    result = pypi.who_owns("unishox2_py3")

    assert result == ["tweedge"]


def test_package_does_not_exist():
    pypi = examiner()
    result = pypi.who_owns("httpxfaster")

    assert result == []