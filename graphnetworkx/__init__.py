"""
graphnetworkx
========

graphnetworkx is a Python package for the creation, manipulation, and study of the
structure, dynamics, and functions of complex networks.

See https://networkx.org for complete documentation.
"""

__version__ = "3.4.14"


def __getattr__(name):
    """Remove functions and provide informative error messages."""
    if name == "nx_yaml":
        raise ImportError(
            "\nThe nx_yaml module has been removed from graphnetworkx.\n"
            "Please use the `yaml` package directly for working with yaml data.\n"
            "For example, a graphnetworkx.Graph `G` can be written to and loaded\n"
            "from a yaml file with:\n\n"
            "    import yaml\n\n"
            "    with open('path_to_yaml_file', 'w') as fh:\n"
            "        yaml.dump(G, fh)\n"
            "    with open('path_to_yaml_file', 'r') as fh:\n"
            "        G = yaml.load(fh, Loader=yaml.Loader)\n\n"
            "Note that yaml.Loader is considered insecure - see the pyyaml\n"
            "documentation for further details.\n\n"
        )
    if name == "read_yaml":
        raise ImportError(
            "\nread_yaml has been removed from graphnetworkx, please use `yaml`\n"
            "directly:\n\n"
            "    import yaml\n\n"
            "    with open('path', 'r') as fh:\n"
            "        yaml.load(fh, Loader=yaml.Loader)\n\n"
            "Note that yaml.Loader is considered insecure - see the pyyaml\n"
            "documentation for further details.\n\n"
        )
    if name == "write_yaml":
        raise ImportError(
            "\nwrite_yaml has been removed from graphnetworkx, please use `yaml`\n"
            "directly:\n\n"
            "    import yaml\n\n"
            "    with open('path_for_yaml_output', 'w') as fh:\n"
            "        yaml.dump(G_to_be_yaml, path_for_yaml_output, **kwds)\n\n"
        )
    raise AttributeError(f"module {__name__} has no attribute {name}")


# These are import orderwise
from graphnetworkx.exception import *

from graphnetworkx import utils

from graphnetworkx import classes
from graphnetworkx.classes import filters
from graphnetworkx.classes import *

from graphnetworkx import convert
from graphnetworkx.convert import *

from graphnetworkx import convert_matrix
from graphnetworkx.convert_matrix import *

from graphnetworkx import relabel
from graphnetworkx.relabel import *

from graphnetworkx import generators
from graphnetworkx.generators import *

from graphnetworkx import readwrite
from graphnetworkx.readwrite import *

# Need to test with SciPy, when available
from graphnetworkx import algorithms
from graphnetworkx.algorithms import *

from graphnetworkx import linalg
from graphnetworkx.linalg import *

from graphnetworkx.testing.test import run as test

from graphnetworkx import drawing
from graphnetworkx.drawing import *
