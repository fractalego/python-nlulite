import logging
import os

from igraph import Graph
from parvusdb import GraphDatabase

_path = os.path.dirname(__file__)


class GraphJoinerVisitor:
    __logger = logging.getLogger(__name__)

    def __init__(self, drs):
        self._rules = """
        CREATE %s;
        """ % str(drs)

    def apply(self, g):
        if not isinstance(g, Graph):
            raise TypeError("DrsRule.apply_to_graph() needs an igraph.Graph as an argument")
        db = GraphDatabase(g)
        lst = db.query(self._rules, repeat_n_times=1)
        return lst