import sys, os, math
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import graph


def er_np(n, p, seed = None):
    """
    Creates a random graph following Erdos-Renyi G(n, p) model.
    :param n: number of nodes
    :param p: probability of an edge existing between any pair of nodes
    :param seed: Seed for generating random number. If it is not specified, time stamp is used.
    :return: a Graph object
    """
    # define an empty graph
    G = graph.Graph({})
    for i in range(n):
        G.add_vertex(i)

    for i in range(n):
        for j in range(i, n):
            pr = np.random.randint(low=0, high=100)

            # if the probability is high enough, add the edge
            if pr - p > 0.0:
                G.add_edge((i, j))

    return G

def er_nm(n, m, seed = None):
    """
    Creates a random graph following Erdos-Renyi G(n,m) model
    :param n: Number of nodes
    :param m: Number of edges
    :param seed: Seed for generating random numbers. If it is not specified, time stamp is used.
    :return: a Graph object
    """

    # create an empty graph with n vertices
    G = graph.Graph({})
    for i in range(n):
        G.add_vertex(i)

    # pick m random pairs without repetition
    edges_to_add = set(np.random.choice(n*(n-1)//2, m, replace=False))

    curr_count = 0
    for i in range(n):
        for j in range(i, n):
            if curr_count in edges_to_add:
                G.add_edge((i,j))

            curr_count += 1

    return G


def compare_edge_count(n, p, seed = None):
    """
    Compares number of edges of G(n,p) and G(n, m) where m = floor(p*C_2^n)
    :param n: Number of nodes
    :param p: Probability of having an edge
    :param seed: Seed for generating random numbers. If it is not specified, time stamp is used
    :return:
    """
    m = p * n * (n-1) / 2
    m = int(math.floor(m))
    G_np = er_np(n, p, seed=seed)
    G_nm = er_nm(n, m, seed=seed)

    ratio = G_np.number_of_edges() / G_nm.number_of_edges()

    return ratio



