"""
====================
Generators - Classic
====================

Unit tests for various classic graph generators in generators/classic.py
"""
import itertools

import pytest
import graphnetworkx as nx
from graphnetworkx.algorithms.isomorphism.isomorph import graph_could_be_isomorphic
from graphnetworkx.utils import nodes_equal, edges_equal

is_isomorphic = graph_could_be_isomorphic


class TestGeneratorClassic:
    def test_balanced_tree(self):
        # balanced_tree(r,h) is a tree with (r**(h+1)-1)/(r-1) edges
        for r, h in [(2, 2), (3, 3), (6, 2)]:
            t = nx.balanced_tree(r, h)
            order = t.order()
            assert order == (r ** (h + 1) - 1) / (r - 1)
            assert nx.is_connected(t)
            assert t.size() == order - 1
            dh = nx.degree_histogram(t)
            assert dh[0] == 0  # no nodes of 0
            assert dh[1] == r ** h  # nodes of degree 1 are leaves
            assert dh[r] == 1  # root is degree r
            assert dh[r + 1] == order - r ** h - 1  # everyone else is degree r+1
            assert len(dh) == r + 2

    def test_balanced_tree_star(self):
        # balanced_tree(r,1) is the r-star
        t = nx.balanced_tree(r=2, h=1)
        assert is_isomorphic(t, nx.star_graph(2))
        t = nx.balanced_tree(r=5, h=1)
        assert is_isomorphic(t, nx.star_graph(5))
        t = nx.balanced_tree(r=10, h=1)
        assert is_isomorphic(t, nx.star_graph(10))

    def test_balanced_tree_path(self):
        """Tests that the balanced tree with branching factor one is the
        path graph.

        """
        # A tree of height four has five levels.
        T = nx.balanced_tree(1, 4)
        P = nx.path_graph(5)
        assert is_isomorphic(T, P)

    def test_full_rary_tree(self):
        r = 2
        n = 9
        t = nx.full_rary_tree(r, n)
        assert t.order() == n
        assert nx.is_connected(t)
        dh = nx.degree_histogram(t)
        assert dh[0] == 0  # no nodes of 0
        assert dh[1] == 5  # nodes of degree 1 are leaves
        assert dh[r] == 1  # root is degree r
        assert dh[r + 1] == 9 - 5 - 1  # everyone else is degree r+1
        assert len(dh) == r + 2

    def test_full_rary_tree_balanced(self):
        t = nx.full_rary_tree(2, 15)
        th = nx.balanced_tree(2, 3)
        assert is_isomorphic(t, th)

    def test_full_rary_tree_path(self):
        t = nx.full_rary_tree(1, 10)
        assert is_isomorphic(t, nx.path_graph(10))

    def test_full_rary_tree_empty(self):
        t = nx.full_rary_tree(0, 10)
        assert is_isomorphic(t, nx.empty_graph(10))
        t = nx.full_rary_tree(3, 0)
        assert is_isomorphic(t, nx.empty_graph(0))

    def test_full_rary_tree_3_20(self):
        t = nx.full_rary_tree(3, 20)
        assert t.order() == 20

    def test_barbell_graph(self):
        # number of nodes = 2*m1 + m2 (2 m1-complete graphs + m2-path + 2 edges)
        # number of edges = 2*(nx.number_of_edges(m1-complete graph) + m2 + 1
        m1 = 3
        m2 = 5
        b = nx.barbell_graph(m1, m2)
        assert nx.number_of_nodes(b) == 2 * m1 + m2
        assert nx.number_of_edges(b) == m1 * (m1 - 1) + m2 + 1

        m1 = 4
        m2 = 10
        b = nx.barbell_graph(m1, m2)
        assert nx.number_of_nodes(b) == 2 * m1 + m2
        assert nx.number_of_edges(b) == m1 * (m1 - 1) + m2 + 1

        m1 = 3
        m2 = 20
        b = nx.barbell_graph(m1, m2)
        assert nx.number_of_nodes(b) == 2 * m1 + m2
        assert nx.number_of_edges(b) == m1 * (m1 - 1) + m2 + 1

        # Raise NetworkXError if m1<2
        m1 = 1
        m2 = 20
        pytest.raises(nx.NetworkXError, nx.barbell_graph, m1, m2)

        # Raise NetworkXError if m2<0
        m1 = 5
        m2 = -2
        pytest.raises(nx.NetworkXError, nx.barbell_graph, m1, m2)

        # nx.barbell_graph(2,m) = nx.path_graph(m+4)
        m1 = 2
        m2 = 5
        b = nx.barbell_graph(m1, m2)
        assert is_isomorphic(b, nx.path_graph(m2 + 4))

        m1 = 2
        m2 = 10
        b = nx.barbell_graph(m1, m2)
        assert is_isomorphic(b, nx.path_graph(m2 + 4))

        m1 = 2
        m2 = 20
        b = nx.barbell_graph(m1, m2)
        assert is_isomorphic(b, nx.path_graph(m2 + 4))

        pytest.raises(
            nx.NetworkXError, nx.barbell_graph, m1, m2, create_using=nx.DiGraph()
        )

        mb = nx.barbell_graph(m1, m2, create_using=nx.MultiGraph())
        assert edges_equal(mb.edges(), b.edges())

    def test_binomial_tree(self):
        graphs = (None, nx.Graph, nx.DiGraph, nx.MultiGraph, nx.MultiDiGraph)
        for create_using in graphs:
            for n in range(0, 4):
                b = nx.binomial_tree(n, create_using)
                assert nx.number_of_nodes(b) == 2 ** n
                assert nx.number_of_edges(b) == (2 ** n - 1)

    def test_complete_graph(self):
        # complete_graph(m) is a connected graph with
        # m nodes and  m*(m+1)/2 edges
        for m in [0, 1, 3, 5]:
            g = nx.complete_graph(m)
            assert nx.number_of_nodes(g) == m
            assert nx.number_of_edges(g) == m * (m - 1) // 2

        mg = nx.complete_graph(m, create_using=nx.MultiGraph)
        assert edges_equal(mg.edges(), g.edges())

        g = nx.complete_graph("abc")
        assert nodes_equal(g.nodes(), ["a", "b", "c"])
        assert g.size() == 3

    def test_complete_digraph(self):
        # complete_graph(m) is a connected graph with
        # m nodes and  m*(m+1)/2 edges
        for m in [0, 1, 3, 5]:
            g = nx.complete_graph(m, create_using=nx.DiGraph)
            assert nx.number_of_nodes(g) == m
            assert nx.number_of_edges(g) == m * (m - 1)

        g = nx.complete_graph("abc", create_using=nx.DiGraph)
        assert len(g) == 3
        assert g.size() == 6
        assert g.is_directed()

    def test_circular_ladder_graph(self):
        G = nx.circular_ladder_graph(5)
        pytest.raises(
            nx.NetworkXError, nx.circular_ladder_graph, 5, create_using=nx.DiGraph
        )
        mG = nx.circular_ladder_graph(5, create_using=nx.MultiGraph)
        assert edges_equal(mG.edges(), G.edges())

    def test_circulant_graph(self):
        # Ci_n(1) is the cycle graph for all n
        Ci6_1 = nx.circulant_graph(6, [1])
        C6 = nx.cycle_graph(6)
        assert edges_equal(Ci6_1.edges(), C6.edges())

        # Ci_n(1, 2, ..., n div 2) is the complete graph for all n
        Ci7 = nx.circulant_graph(7, [1, 2, 3])
        K7 = nx.complete_graph(7)
        assert edges_equal(Ci7.edges(), K7.edges())

        # Ci_6(1, 3) is K_3,3 i.e. the utility graph
        Ci6_1_3 = nx.circulant_graph(6, [1, 3])
        K3_3 = nx.complete_bipartite_graph(3, 3)
        assert is_isomorphic(Ci6_1_3, K3_3)

    def test_cycle_graph(self):
        G = nx.cycle_graph(4)
        assert edges_equal(G.edges(), [(0, 1), (0, 3), (1, 2), (2, 3)])
        mG = nx.cycle_graph(4, create_using=nx.MultiGraph)
        assert edges_equal(mG.edges(), [(0, 1), (0, 3), (1, 2), (2, 3)])
        G = nx.cycle_graph(4, create_using=nx.DiGraph)
        assert not G.has_edge(2, 1)
        assert G.has_edge(1, 2)
        assert G.is_directed()

        G = nx.cycle_graph("abc")
        assert len(G) == 3
        assert G.size() == 3
        g = nx.cycle_graph("abc", nx.DiGraph)
        assert len(g) == 3
        assert g.size() == 3
        assert g.is_directed()

    def test_dorogovtsev_goltsev_mendes_graph(self):
        G = nx.dorogovtsev_goltsev_mendes_graph(0)
        assert edges_equal(G.edges(), [(0, 1)])
        assert nodes_equal(list(G), [0, 1])
        G = nx.dorogovtsev_goltsev_mendes_graph(1)
        assert edges_equal(G.edges(), [(0, 1), (0, 2), (1, 2)])
        assert nx.average_clustering(G) == 1.0
        assert sorted(nx.triangles(G).values()) == [1, 1, 1]
        G = nx.dorogovtsev_goltsev_mendes_graph(10)
        assert nx.number_of_nodes(G) == 29526
        assert nx.number_of_edges(G) == 59049
        assert G.degree(0) == 1024
        assert G.degree(1) == 1024
        assert G.degree(2) == 1024

        pytest.raises(
            nx.NetworkXError,
            nx.dorogovtsev_goltsev_mendes_graph,
            7,
            create_using=nx.DiGraph,
        )
        pytest.raises(
            nx.NetworkXError,
            nx.dorogovtsev_goltsev_mendes_graph,
            7,
            create_using=nx.MultiGraph,
        )

    def test_create_using(self):
        G = nx.empty_graph()
        assert isinstance(G, nx.Graph)
        pytest.raises(TypeError, nx.empty_graph, create_using=0.0)
        pytest.raises(TypeError, nx.empty_graph, create_using="Graph")

        G = nx.empty_graph(create_using=nx.MultiGraph)
        assert isinstance(G, nx.MultiGraph)
        G = nx.empty_graph(create_using=nx.DiGraph)
        assert isinstance(G, nx.DiGraph)

        G = nx.empty_graph(create_using=nx.DiGraph, default=nx.MultiGraph)
        assert isinstance(G, nx.DiGraph)
        G = nx.empty_graph(create_using=None, default=nx.MultiGraph)
        assert isinstance(G, nx.MultiGraph)
        G = nx.empty_graph(default=nx.MultiGraph)
        assert isinstance(G, nx.MultiGraph)

        G = nx.path_graph(5)
        H = nx.empty_graph(create_using=G)
        assert not H.is_multigraph()
        assert not H.is_directed()
        assert len(H) == 0
        assert G is H

        H = nx.empty_graph(create_using=nx.MultiGraph())
        assert H.is_multigraph()
        assert not H.is_directed()
        assert G is not H

    def test_empty_graph(self):
        G = nx.empty_graph()
        assert nx.number_of_nodes(G) == 0
        G = nx.empty_graph(42)
        assert nx.number_of_nodes(G) == 42
        assert nx.number_of_edges(G) == 0

        G = nx.empty_graph("abc")
        assert len(G) == 3
        assert G.size() == 0

        # create empty digraph
        G = nx.empty_graph(42, create_using=nx.DiGraph(name="duh"))
        assert nx.number_of_nodes(G) == 42
        assert nx.number_of_edges(G) == 0
        assert isinstance(G, nx.DiGraph)

        # create empty multigraph
        G = nx.empty_graph(42, create_using=nx.MultiGraph(name="duh"))
        assert nx.number_of_nodes(G) == 42
        assert nx.number_of_edges(G) == 0
        assert isinstance(G, nx.MultiGraph)

        # create empty graph from another
        pete = nx.petersen_graph()
        G = nx.empty_graph(42, create_using=pete)
        assert nx.number_of_nodes(G) == 42
        assert nx.number_of_edges(G) == 0
        assert isinstance(G, nx.Graph)

    def test_ladder_graph(self):
        for i, G in [
            (0, nx.empty_graph(0)),
            (1, nx.path_graph(2)),
            (2, nx.hypercube_graph(2)),
            (10, nx.grid_graph([2, 10])),
        ]:
            assert is_isomorphic(nx.ladder_graph(i), G)

        pytest.raises(nx.NetworkXError, nx.ladder_graph, 2, create_using=nx.DiGraph)

        g = nx.ladder_graph(2)
        mg = nx.ladder_graph(2, create_using=nx.MultiGraph)
        assert edges_equal(mg.edges(), g.edges())

    def test_lollipop_graph(self):
        # number of nodes = m1 + m2
        # number of edges = nx.number_of_edges(nx.complete_graph(m1)) + m2
        for m1, m2 in [(3, 5), (4, 10), (3, 20)]:
            b = nx.lollipop_graph(m1, m2)
            assert nx.number_of_nodes(b) == m1 + m2
            assert nx.number_of_edges(b) == m1 * (m1 - 1) / 2 + m2

        # Raise NetworkXError if m<2
        pytest.raises(nx.NetworkXError, nx.lollipop_graph, 1, 20)

        # Raise NetworkXError if n<0
        pytest.raises(nx.NetworkXError, nx.lollipop_graph, 5, -2)

        # lollipop_graph(2,m) = path_graph(m+2)
        for m1, m2 in [(2, 5), (2, 10), (2, 20)]:
            b = nx.lollipop_graph(m1, m2)
            assert is_isomorphic(b, nx.path_graph(m2 + 2))

        pytest.raises(
            nx.NetworkXError, nx.lollipop_graph, m1, m2, create_using=nx.DiGraph
        )

        mb = nx.lollipop_graph(m1, m2, create_using=nx.MultiGraph)
        assert edges_equal(mb.edges(), b.edges())

        g = nx.lollipop_graph([1, 2, 3, 4], "abc")
        assert len(g) == 7
        assert g.size() == 9

    def test_null_graph(self):
        assert nx.number_of_nodes(nx.null_graph()) == 0

    def test_path_graph(self):
        p = nx.path_graph(0)
        assert is_isomorphic(p, nx.null_graph())

        p = nx.path_graph(1)
        assert is_isomorphic(p, nx.empty_graph(1))

        p = nx.path_graph(10)
        assert nx.is_connected(p)
        assert sorted(d for n, d in p.degree()) == [1, 1, 2, 2, 2, 2, 2, 2, 2, 2]
        assert p.order() - 1 == p.size()

        dp = nx.path_graph(3, create_using=nx.DiGraph)
        assert dp.has_edge(0, 1)
        assert not dp.has_edge(1, 0)

        mp = nx.path_graph(10, create_using=nx.MultiGraph)
        assert edges_equal(mp.edges(), p.edges())

        G = nx.path_graph("abc")
        assert len(G) == 3
        assert G.size() == 2
        g = nx.path_graph("abc", nx.DiGraph)
        assert len(g) == 3
        assert g.size() == 2
        assert g.is_directed()

    def test_star_graph(self):
        star_graph = nx.star_graph
        assert is_isomorphic(star_graph(0), nx.empty_graph(1))
        assert is_isomorphic(star_graph(1), nx.path_graph(2))
        assert is_isomorphic(star_graph(2), nx.path_graph(3))
        assert is_isomorphic(star_graph(5), nx.complete_bipartite_graph(1, 5))

        s = star_graph(10)
        assert sorted(d for n, d in s.degree()) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10]

        pytest.raises(nx.NetworkXError, star_graph, 10, create_using=nx.DiGraph)

        ms = star_graph(10, create_using=nx.MultiGraph)
        assert edges_equal(ms.edges(), s.edges())

        G = star_graph("abcdefg")
        assert len(G) == 7
        assert G.size() == 6

    def test_trivial_graph(self):
        assert nx.number_of_nodes(nx.trivial_graph()) == 1

    def test_turan_graph(self):
        assert nx.number_of_edges(nx.turan_graph(13, 4)) == 63
        assert is_isomorphic(
            nx.turan_graph(13, 4), nx.complete_multipartite_graph(3, 4, 3, 3)
        )

    def test_wheel_graph(self):
        for n, G in [
            (0, nx.null_graph()),
            (1, nx.empty_graph(1)),
            (2, nx.path_graph(2)),
            (3, nx.complete_graph(3)),
            (4, nx.complete_graph(4)),
        ]:
            g = nx.wheel_graph(n)
            assert is_isomorphic(g, G)

        g = nx.wheel_graph(10)
        assert sorted(d for n, d in g.degree()) == [3, 3, 3, 3, 3, 3, 3, 3, 3, 9]

        pytest.raises(nx.NetworkXError, nx.wheel_graph, 10, create_using=nx.DiGraph)

        mg = nx.wheel_graph(10, create_using=nx.MultiGraph())
        assert edges_equal(mg.edges(), g.edges())

        G = nx.wheel_graph("abc")
        assert len(G) == 3
        assert G.size() == 3

    def test_complete_0_partite_graph(self):
        """Tests that the complete 0-partite graph is the null graph."""
        G = nx.complete_multipartite_graph()
        H = nx.null_graph()
        assert nodes_equal(G, H)
        assert edges_equal(G.edges(), H.edges())

    def test_complete_1_partite_graph(self):
        """Tests that the complete 1-partite graph is the empty graph."""
        G = nx.complete_multipartite_graph(3)
        H = nx.empty_graph(3)
        assert nodes_equal(G, H)
        assert edges_equal(G.edges(), H.edges())

    def test_complete_2_partite_graph(self):
        """Tests that the complete 2-partite graph is the complete bipartite
        graph.

        """
        G = nx.complete_multipartite_graph(2, 3)
        H = nx.complete_bipartite_graph(2, 3)
        assert nodes_equal(G, H)
        assert edges_equal(G.edges(), H.edges())

    def test_complete_multipartite_graph(self):
        """Tests for generating the complete multipartite graph."""
        G = nx.complete_multipartite_graph(2, 3, 4)
        blocks = [(0, 1), (2, 3, 4), (5, 6, 7, 8)]
        # Within each block, no two vertices should be adjacent.
        for block in blocks:
            for u, v in itertools.combinations_with_replacement(block, 2):
                assert v not in G[u]
                assert G.nodes[u] == G.nodes[v]
        # Across blocks, all vertices should be adjacent.
        for (block1, block2) in itertools.combinations(blocks, 2):
            for u, v in itertools.product(block1, block2):
                assert v in G[u]
                assert G.nodes[u] != G.nodes[v]
