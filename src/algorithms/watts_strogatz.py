import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import graph
import numpy as np


def watts_strogatz(n, k, beta):
    """
    Creates a random graph following Watts-Strogatz model
    :param n: (integer) Number of vertices.
    :param k: (integer) Number of neighbours. Must be even.
    :param beta: (float) rewiring probability
    :return: (Graph) a graph object
    """
    assert k % 2 == 0
    assert 0.0 <= beta <= 1.0


