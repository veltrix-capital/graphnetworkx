"""
Flow Hierarchy.
"""
import graphnetworkx as nx

__all__ = ["flow_hierarchy"]


def flow_hierarchy(G, weight=None):
    """Returns the flow hierarchy of a directed network.

    Flow hierarchy is defined as the fraction of edges not participating
    in cycles in a directed graph [1]_.

    Parameters
    ----------
    G : DiGraph or MultiDiGraph
       A directed graph

    weight : key,optional (default=None)
       Attribute to use for node weights. If None the weight defaults to 1.

    Returns
    -------
    h : float
       Flow hierarchy value

    Notes
    -----
    The algorithm described in [1]_ computes the flow hierarchy through
    exponentiation of the adjacency matrix.  This function implements an
    alternative approach that finds strongly connected components.
    An edge is in a cycle if and only if it is in a strongly connected
    component, which can be found in $O(m)$ time using Tarjan's algorithm.

    References
    ----------
    .. [1] Luo, J.; Magee, C.L. (2011),
       Detecting evolving patterns of self-organizing networks by flow
       hierarchy measurement, Complexity, Volume 16 Issue 6 53-61.
       DOI: 10.1002/cplx.20368
       http://web.mit.edu/~cmagee/www/documents/28-DetectingEvolvingPatterns_FlowHierarchy.pdf
    """
    if not G.is_directed():
        raise nx.NetworkXError("G must be a digraph in flow_hierarchy")
    scc = nx.strongly_connected_components(G)
    return 1.0 - sum(G.subgraph(c).size(weight) for c in scc) / float(G.size(weight))
