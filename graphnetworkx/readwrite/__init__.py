"""
A package for reading and writing graphs in various formats.

"""


def __getattr__(name):
    """Remove functions and provide informative error messages."""
    if name == "nx_yaml":
        raise ImportError(
            "\nThe nx_yaml module has been removed from graphnetworkx.\n"
            "Please use the `yaml` package directly for working with yaml data.\n"
            "For example, a networkx.Graph `G` can be written to and loaded\n"
            "from a yaml file with:\n\n"
            "    import yaml\n\n"
            "    with open('path_to_yaml_file', 'w') as fh:\n"
            "        yaml.dump(G, fh)\n"
            "    with open('path_to_yaml_file', 'r') as fh:\n"
            "        G = yaml.load(fh, Loader=yaml.Loader)\n\n"
            "Note that yaml.Loader is considered insecure - see the pyyaml\n"
            "documentation for further details.\n\n"
            "This message will be removed in NetworkX 3.0."
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
            "This message will be removed in NetworkX 3.0."
        )
    if name == "write_yaml":
        raise ImportError(
            "\nwrite_yaml has been removed from graphnetworkx, please use `yaml`\n"
            "directly:\n\n"
            "    import yaml\n\n"
            "    with open('path_for_yaml_output', 'w') as fh:\n"
            "        yaml.dump(G_to_be_yaml, path_for_yaml_output, **kwds)\n\n"
            "This message will be removed in NetworkX 3.0."
        )
    raise AttributeError(f"module {__name__} has no attribute {name}")


from graphnetworkx.readwrite.adjlist import *
from graphnetworkx.readwrite.multiline_adjlist import *
from graphnetworkx.readwrite.edgelist import *
from graphnetworkx.readwrite.gpickle import *
from graphnetworkx.readwrite.pajek import *
from graphnetworkx.readwrite.leda import *
from graphnetworkx.readwrite.sparse6 import *
from graphnetworkx.readwrite.graph6 import *
from graphnetworkx.readwrite.gml import *
from graphnetworkx.readwrite.graphml import *
from graphnetworkx.readwrite.gexf import *
from graphnetworkx.readwrite.nx_shp import *
from graphnetworkx.readwrite.json_graph import *
from graphnetworkx.readwrite.text import *
