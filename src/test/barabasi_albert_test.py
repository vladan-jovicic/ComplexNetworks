import unittest
import sys

sys.path.insert(0, '../')
import graph
import algorithms.barabasi_albert as brb_alb


class BarabasiAlbert(unittest.TestCase):

    def test_init(self):
        g = brb_alb.barabasi_albert(10, 2)
        self.assertEqual(2, 2)
