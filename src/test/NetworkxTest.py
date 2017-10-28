import unittest
import os, sys
import networkx as nx
import random

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import graph

class GraphTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        filename = "../../test_data/graph_1000n_4000m.txt"
        super(GraphTest, cls).setUpClass()
        cls.graph = graph.Graph()
        cls.graph.read_from_file(filename=filename)
        cls.nxgraph = nx.Graph()
        for u, v in cls.graph.edges():
            cls.nxgraph.add_edge(u, v)

    def test_vertex_degree(self):
        # pick random vertex and test it
        rnd_vertex = str(random.randint(1, self.graph.number_of_vertices()))
        my_lib_ans = self.graph.vertex_degree(rnd_vertex)
        nx_ans = self.nxgraph.degree(rnd_vertex)
        self.assertEqual(my_lib_ans, nx_ans)
        self.assertRaises(KeyError,self.graph.vertex_degree, "l")

    def test_isolated_vertices(self):
        my_ans = self.graph.find_isolated_vertices()
        nx_ans = nx.isolates(self.nxgraph)
        self.assertItemsEqual(nx_ans, my_ans)

    def test_density(self):
        my_ans = self.graph.density()
        nx_ans = nx.density(self.nxgraph)
        self.assertEqual(my_ans, nx_ans)

    def test_erdos_gallai(self):
        deg_seq = self.graph.degree_sequence()
        my_ans = self.graph.erdos_gallai(degree_seq=deg_seq)
        nx_ans = nx.is_valid_degree_sequence_erdos_gallai(deg_seq)
        self.assertEqual(my_ans, nx_ans)

    #def test_clustering(self):
    #    self.assertEqual(self.graph.global_clustering_coefficient(), 0.5)

    def test_shortest_path_uv(self):
        # picks two random vertices and tests the shortest path
        rnd_vertex1 = str(random.randint(1, self.graph.number_of_vertices()))
        rnd_vertex2 = str(random.randint(1, self.graph.number_of_vertices()))
        my_ans = self.graph.shortest_path(rnd_vertex1, rnd_vertex2)
        nx_ans = nx.shortest_path(self.nxgraph, rnd_vertex1, rnd_vertex2)
        self.assertEqual(my_ans, len(nx_ans)-1)

    def test_diameter(self):
        self.assertEqual(self.graph.diameter(), nx.diameter(self.nxgraph))

    #def test_spanning_tree(self):
    #    s_tree = self.graph.spanning_tree()
    #    self.assertEqual(len(s_tree), self.graph.number_of_vertices() - 1)

if __name__ == "__main__":
    unittest.main()