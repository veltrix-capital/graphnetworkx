from glob import glob
import os
import sys
from setuptools import setup

if sys.version_info[:2] < (3, 7):
    error = (
        "graphnetworkx 3.4+ requires Python 3.7 or later (%d.%d detected). \n"
    )
    sys.stderr.write(error + "\n")
    sys.exit(1)


name = "graphnetworkx"
description = "Python package for creating and manipulating graphs and networks"
authors = {
    "Hagberg": ("John", "john@veltrixcap.org"),
}
maintainer = "Graphnetworkx Developers"
maintainer_email = "graphnetworkx-discuss@googlegroups.com"
url = "https://networkx.org/"
project_urls = {
    "Bug Tracker": "https://github.com/taylortech75/graphnetworkx/issues",
    "Documentation": "https://networkx.org/documentation/stable/",
    "Source Code": "https://github.com/taylortech75/graphnetworkx",
}
platforms = ["Linux", "Mac OSX", "Windows", "Unix"]
keywords = [
    "Networks",
    "Graph Theory",
    "Mathematics",
    "network",
    "graph",
    "discrete mathematics",
    "math",
]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3 :: Only",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Scientific/Engineering :: Bio-Informatics",
    "Topic :: Scientific/Engineering :: Information Analysis",
    "Topic :: Scientific/Engineering :: Mathematics",
    "Topic :: Scientific/Engineering :: Physics",
]

with open("graphnetworkx/__init__.py") as fid:
    for line in fid:
        if line.startswith("__version__"):
            version = line.strip().split()[-1][1:-1]
            break

packages = [
    "graphnetworkx",
    "graphnetworkx.algorithms",
    "graphnetworkx.algorithms.assortativity",
    "graphnetworkx.algorithms.bipartite",
    "graphnetworkx.algorithms.node_classification",
    "graphnetworkx.algorithms.centrality",
    "graphnetworkx.algorithms.community",
    "graphnetworkx.algorithms.components",
    "graphnetworkx.algorithms.connectivity",
    "graphnetworkx.algorithms.coloring",
    "graphnetworkx.algorithms.flow",
    "graphnetworkx.algorithms.minors",
    "graphnetworkx.algorithms.traversal",
    "graphnetworkx.algorithms.isomorphism",
    "graphnetworkx.algorithms.shortest_paths",
    "graphnetworkx.algorithms.link_analysis",
    "graphnetworkx.algorithms.operators",
    "graphnetworkx.algorithms.approximation",
    "graphnetworkx.algorithms.tree",
    "graphnetworkx.classes",
    "graphnetworkx.generators",
    "graphnetworkx.drawing",
    "graphnetworkx.linalg",
    "graphnetworkx.readwrite",
    "graphnetworkx.readwrite.json_graph",
    "graphnetworkx.tests",
    "graphnetworkx.testing",
    "graphnetworkx.utils",
]

docdirbase = "share/doc/graphnetworkx-%s" % version
# add basic documentation
data = [(docdirbase, glob("*.txt"))]
# add examples
for d in [
    ".",
    "advanced",
    "algorithms",
    "basic",
    "3d_drawing",
    "drawing",
    "graph",
    "javascript",
    "jit",
    "pygraphviz",
    "subclass",
]:
    dd = os.path.join(docdirbase, "examples", d)
    pp = os.path.join("examples", d)
    data.append((dd, glob(os.path.join(pp, "*.txt"))))
    data.append((dd, glob(os.path.join(pp, "*.py"))))
    data.append((dd, glob(os.path.join(pp, "*.bz2"))))
    data.append((dd, glob(os.path.join(pp, "*.gz"))))
    data.append((dd, glob(os.path.join(pp, "*.mbox"))))
    data.append((dd, glob(os.path.join(pp, "*.edgelist"))))
# add js force examples
dd = os.path.join(docdirbase, "examples", "javascript/force")
pp = os.path.join("examples", "javascript/force")
data.append((dd, glob(os.path.join(pp, "*"))))

# add the tests
package_data = {
    "graphnetworkx": ["tests/*.py"],
    "graphnetworkx.algorithms": ["tests/*.py"],
    "graphnetworkx.algorithms.assortativity": ["tests/*.py"],
    "graphnetworkx.algorithms.bipartite": ["tests/*.py"],
    "graphnetworkx.algorithms.node_classification": ["tests/*.py"],
    "graphnetworkx.algorithms.centrality": ["tests/*.py"],
    "graphnetworkx.algorithms.community": ["tests/*.py"],
    "graphnetworkx.algorithms.components": ["tests/*.py"],
    "graphnetworkx.algorithms.connectivity": ["tests/*.py"],
    "graphnetworkx.algorithms.coloring": ["tests/*.py"],
    "graphnetworkx.algorithms.minors": ["tests/*.py"],
    "graphnetworkx.algorithms.flow": ["tests/*.py", "tests/*.bz2"],
    "graphnetworkx.algorithms.isomorphism": ["tests/*.py", "tests/*.*99"],
    "graphnetworkx.algorithms.link_analysis": ["tests/*.py"],
    "graphnetworkx.algorithms.approximation": ["tests/*.py"],
    "graphnetworkx.algorithms.operators": ["tests/*.py"],
    "graphnetworkx.algorithms.shortest_paths": ["tests/*.py"],
    "graphnetworkx.algorithms.traversal": ["tests/*.py"],
    "graphnetworkx.algorithms.tree": ["tests/*.py"],
    "graphnetworkx.classes": ["tests/*.py"],
    "graphnetworkx.generators": ["tests/*.py", "atlas.dat.gz"],
    "graphnetworkx.drawing": ["tests/*.py"],
    "graphnetworkx.linalg": ["tests/*.py"],
    "graphnetworkx.readwrite": ["tests/*.py"],
    "graphnetworkx.readwrite.json_graph": ["tests/*.py"],
    "graphnetworkx.testing": ["tests/*.py"],
    "graphnetworkx.utils": ["tests/*.py", "*.pem"],
}


def parse_requirements_file(filename):
    with open(filename) as fid:
        requires = [l.strip() for l in fid.readlines() if not l.startswith("#")]

    return requires


install_requires = []
extras_require = {
    dep: parse_requirements_file("requirements/" + dep + ".txt")
    for dep in ["default", "developer", "doc", "extra", "test"]
}

with open("README.rst", "r") as fh:
    long_description = fh.read()

if __name__ == "__main__":

    setup(
        name=name,
        version=version,
        maintainer=maintainer,
        maintainer_email=maintainer_email,
        author=authors["Hagberg"][0],
        author_email=authors["Hagberg"][1],
        description=description,
        keywords=keywords,
        long_description=long_description,
        platforms=platforms,
        url=url,
        project_urls=project_urls,
        classifiers=classifiers,
        packages=packages,
        data_files=data,
        package_data=package_data,
        install_requires=install_requires,
        extras_require=extras_require,
        python_requires=">=3.7",
        zip_safe=False,
    )
