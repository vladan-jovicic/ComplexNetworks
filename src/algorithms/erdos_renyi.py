"""
Erdos-Renyi Model
----------------------
This module contains different functions for generating a random graphs
using Erdos-Renyi models G(n, p) and G(n, m)
"""
import sys, os, math
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import graph


def er_np(n, p, seed=None):
    """
    Creates a random graph following Erdos-Renyi G(n, p) model.

    :param n: number of nodes
    :param p: probability of an edge existing between any pair of nodes
    :param seed: Seed for generating random number. If it is not specified, time stamp is used.
    :return: a Graph object
    """

    G = graph.Graph({})
    for i in range(n):
        G.add_vertex(i)

    # generate n choose 2 random integers
    probabilities = np.random.randint(low=0, high=100, size=n*(n-1)//2)

    for u in range(n):
        for v in range(u+1, n):
            proba = np.random.uniform()
            if float(p) - proba > float(0.0):
                G.add_edge((u, v))

    # edge k has points i = floor((-1 + sqrt(1 + 8k))/2)
    # and j = k - i*(i+1) / 2

    return G


def er_nm(n, m, seed=None):
    """
    Creates a random graph following Erdos-Renyi G(n,m) model.

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
    edges_to_add = np.random.choice(1+np.arange(n*(n-1)//2), m, replace=False)

    # think about it as a matrix
    # which is lower - right triangular
    for e in edges_to_add:
        i = (-1 + math.sqrt(1 + 8*e))/2.0
        i = int(math.ceil(i))
        j = e - i*(i-1)//2
        G.add_edge((i-1, j-1))

    return G


def compare_edge_count(n, p, seed=None):
    """
    Compares number of edges of G(n,p) and G(n, m) where m = floor(p*C_2^n)

    :param n: Number of nodes
    :param p: Probability of having an edge
    :param seed: Seed for generating random numbers. If it is not specified, time stamp is used
    :return: the ratio suze(E(G(n, p))) / size(E(G(n, m)))
    """
    m = p * n * (n-1) / 2
    m = int(math.floor(m))
    G_np = er_np(n, p, seed=seed)
    G_nm = er_nm(n, m, seed=seed)

    ratio = G_np.number_of_edges() / G_nm.number_of_edges()

    return ratio

