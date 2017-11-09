import unittest, os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import algorithms.erdos_renyi as erm



class ERTest(unittest.TestCase):

    def test_simple(self):
        n, p = 10, 0.5
        G = erm.er_np(n, p)
        self.assertEqual(n, G.number_of_vertices())

    def test_er_nm(self):
        n, m = 10, 11
        G = erm.er_nm(n, m)
        self.assertEqual(m, G.number_of_edges())

    def test_compare_edges(self):
        n, p = 10, 0.5

        ratio = erm.compare_edge_count(n, p)
        self.assertGreater(ratio, 0, msg="Ration is greater than zero")


if __name__ == "__main__":
    unittest.main()
