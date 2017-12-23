import unittest, os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import algorithms.watts_strogatz as ws


class WSTest(unittest.TestCase):

    def test_init(self):
        g = ws.watts_strogatz(10, 4, 0.5)
        print(g.edges())
        print(g.global_clustering_coefficient())
        print(g.shortest_path())
        print(g.diameter())
        self.assertEqual(g.number_of_edges(), 20)

