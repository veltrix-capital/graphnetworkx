import pytest


def test_utils_namespace():
    """Ensure objects are not unintentionally exposed in utils namespace."""
    with pytest.raises(ImportError):
        from graphnetworkx.utils import nx
    with pytest.raises(ImportError):
        from graphnetworkx.utils import sys
    with pytest.raises(ImportError):
        from graphnetworkx.utils import defaultdict, deque
