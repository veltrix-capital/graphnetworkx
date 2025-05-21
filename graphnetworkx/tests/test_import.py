import pytest


def test_namespace_alias():
    with pytest.raises(ImportError):
        from graphnetworkx import nx


def test_namespace_nesting():
    with pytest.raises(ImportError):
        from graphnetworkx.exception import NetworkX
