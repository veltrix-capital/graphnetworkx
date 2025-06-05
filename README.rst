Graphnetworkx
=============

.. image:: https://codecov.io/gh/taylortech75/graphnetworkx/branch/main/graph/badge.svg
   :target: https://app.codecov.io/gh/taylortech75/graphnetworkx/branch/main

.. image:: https://img.shields.io/github/labels/taylortech75/graphnetworkx/Good%20First%20Issue?color=green&label=Contribute%20&style=flat-square
   :target: https://github.com/taylortech75/graphnetworkx/issues?q=is%3Aopen+is%3Aissue+label%3A%22Good+First+Issue%22

**Graphnetworkx** is a Python package for the creation, manipulation,  
and study of the structure, dynamics, and functions of complex networks.

- **Website (including documentation):** https://networkx.org  
- **Mailing list:** https://groups.google.com/forum/#!forum/networkx-discuss  
- **Source:** https://github.com/veltrix-capital/graphnetworkx  
- **Bug reports:** https://github.com/veltrix-capital/graphnetworkx/issues  
- **Tutorial:** https://networkx.org/documentation/latest/tutorial.html  
- **GitHub Discussions:** https://github.com/veltrix-capital/graphnetworkx/discussions  

Simple Example
--------------

Find the shortest path between two nodes in an undirected graph:

.. code:: python

   >>> import graphnetworkx as nx
   >>> G = nx.Graph()
   >>> G.add_edge('A', 'B', weight=4)
   >>> G.add_edge('B', 'D', weight=2)
   >>> G.add_edge('A', 'C', weight=3)
   >>> G.add_edge('C', 'D', weight=4)
   >>> nx.shortest_path(G, 'A', 'D', weight='weight')
   ['A', 'B', 'D']

Install
-------

Install the latest version of graphnetworkx:

.. code:: shell

   $ pip install graphnetworkx

Install with all optional dependencies:

.. code:: shell

   $ pip install graphnetworkx[all]

For additional details, please see `INSTALL.rst`.

Bugs
----

Please report any bugs that you find `here <https://github.com/taylortech75/graphnetworkx/issues>`_.  
Or, even better, fork the repository on `GitHub <https://github.com/taylortech75/graphnetworkx>`_  
and create a pull request (PR). We welcome all changes, big or small, and we  
will help you make the PR if you are new to `git` (just ask on the issue and/or  
see `CONTRIBUTING.rst`).

License
-------

Released under the 3-Clause BSD license (see `LICENSE.txt`):

.. code:: text

   Copyright (C) 2004-2021 graphnetworkx Developers  
   John <john@veltrixcap.org>
