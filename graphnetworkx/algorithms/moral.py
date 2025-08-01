r"""Function for computing the moral graph of a directed graph."""

from graphnetworkx.utils import not_implemented_for
import itertools

__all__ = ["moral_graph"]


@not_implemented_for("undirected")
def moral_graph(G):
    r"""Return the Moral Graph

    Returns the moralized graph of a given directed graph.

    Parameters
    ----------
    G : NetworkX graph
        Directed graph

    Returns
    -------
    H : NetworkX graph
        The undirected moralized graph of G

    Notes
    -----
    A moral graph is an undirected graph H = (V, E) generated from a
    directed Graph, where if a node has more than one parent node, edges
    between these parent nodes are inserted and all directed edges become
    undirected.

    https://en.wikipedia.org/wiki/Moral_graph

    References
    ----------
    .. [1] Wray L. Buntine. 1995. Chain graphs for learning.
           In Proceedings of the Eleventh conference on Uncertainty
           in artificial intelligence (UAI'95)
    """
    if G is None:
        raise ValueError("Expected NetworkX graph!")

    H = G.to_undirected()
    for preds in G.pred.values():
        predecessors_combinations = itertools.combinations(preds, r=2)
        H.add_edges_from(predecessors_combinations)
    return H
