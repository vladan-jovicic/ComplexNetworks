import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import graph
import numpy as np
from scipy.linalg import circulant


def _distance_matrix(n):
    Dmax = n // 2

    D = range(Dmax + 1)
    # this creates [0, 1, ... , n//2, n//2-1, ..., 1]
    D += D[-2 + (n % 2):0:-1]

    return circulant(D) / Dmax


def _pd(d, p0, beta):
    # beta times edge density +
    return beta * p0 + (d <= p0) * (1 - beta)


def watts_strogatz(n, k, beta, seed=1):
    """
    Creates a random graph following Watts-Strogatz model.
    :param n: (integer) Number of vertices.
    :param k: (integer) Number of neighbours. Must be even.
    :param beta: (float) rewiring probability
    :return: (Graph) a graph object
    """
    assert k % 2 == 0
    assert 0.0 <= beta <= 1.0

    vertices = set(range(n))
    rng = np.random.RandomState(seed)

    ring = create_regular_ring_lattice(n, k)
    ring_edges = ring.edges()

    ws_graph = graph.Graph({})

    for u in range(n):
        u_neighbors = ring.get_neighbors(u)

        for v in u_neighbors:
            proba = np.random.uniform(0.0, 1.0)
            if proba > beta:
                continue
            u_current_neighbors = ring.get_neighbors(u)
            u_neighbors_set = set(u_current_neighbors)
            v_neighbors = set(ring.get_neighbors(v))
            non_neighbors = list(vertices.difference(u_current_neighbors))

            # pick one of the non neighbors
            new_v = np.random.choice(non_neighbors)
            # remove v from my neighbors
            u_neighbors_set.remove(v)
            u_neighbors_set.add(new_v)
            v_neighbors.remove(u)

            ring.update_neighbors(u, list(u_current_neighbors))
            ring.update_neighbors(v, list(v_neighbors))

    return ring


def create_regular_ring_lattice(n, k):
    """
    Creates a regular ring lattice graphs.
    :param n: (integer) Number of vertices.
    :param k: (integer) Number of neighbours.
    :return: a Graph instance representing the ring graph.
    """
    g = graph.Graph({})

    for i in range(n):
        for j in range(1, k//2 + 1):
            u, v = i, (i + j) % n
            g.add_edge((u, v))

    return g


