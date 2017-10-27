import unittest
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import graph

class GraphTest(unittest.TestCase):

    def setUp(self):
        G = {
            "a": ["c", "d", "g"],
            "b": ["c", "f"],
            "c": ["a", "b", "d", "f"],
            "d": ["a", "c", "e", "g"],
            "e": ["d"],
            "f": ["b", "c"],
            "g": ["a", "d"]
        }
        self.graph = graph.Graph(G)
        self.empty = graph.Graph()
        #self.complete = graph.Graph()

    def test_vertex_degree(self):
        self.assertEqual(self.graph.vertex_degree("a"), 3)
        self.assertRaises(KeyError,self.graph.vertex_degree, "l")

    def test_isolated_vertices(self):
        self.assertEqual(self.graph.find_isolated_vertices(), [])

    def test_density(self):
        self.assertEqual(self.graph.number_of_edges(), 9)
        self.assertEqual(self.graph.number_of_vertices(), 7)
        self.assertEqual(self.graph.density(), 9.0 / 21.0)

    def test_degree_seq(self):
        self.assertEqual(self.graph.degree_sequence(), [4, 4, 3, 2, 2, 2, 1])

    def test_erdos_gallai(self):
        self.assertTrue(self.graph.erdos_gallai())
        self.assertTrue(self.empty.erdos_gallai([0]))

    def test_clustering(self):
        self.assertEqual(self.graph.global_clustering_coefficient(), 0.5)
        self.assertEqual(self.empty.global_clustering_coefficient(), 0.0)

    def test_shortest_path_uv(self):
        self.assertEqual(self.graph.shortest_path(u="a", v="b"), 2)

    def test_diameter(self):
        self.assertEqual(self.graph.diameter(), 3)

    def test_spanning_tree(self):
        s_tree = self.graph.spanning_tree()
        self.assertEqual(len(s_tree), self.graph.number_of_vertices() - 1)

if __name__ == "__main__":
    unittest.main()
