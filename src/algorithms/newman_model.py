"""
Newman Model
-----------------------
This module contains a functions for generating random graph
using configuration model. In configuration model, one represents
a graph using degree sequence. The actual graph is obtained by randomly
connecting stubs of vertices.
"""

import sys, os, math
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def degree_sequence_regular(n, k):
    """
    Generates a degree sequnce following k-regular distribution

    :param n: Number of vertices.
    :param k: The parameter k for k-regular distribution
    :return: A list containing n integers representing degrees of vertices following k-regular distribution.
    """
    return [k] * n


def degree_sequence_lognormal(n, mu, sigma):
    """
    Generates a degree sequnce following k-regular distribution

    :param n: Number of vertices.
    :param mu: The parameter mu for lognormal distribution
    :param sigma: The parameter sigma for lognormal distribution
    :return: A list containing n integers representing degrees of vertices following lognormal distribution
    """
    degree_seq = np.random.normal(mu, sigma, size=n)
    return degree_seq


def configure_sequence(degree_seq):
    """
    Given a degree sequence, creates a random graph following configuration
    model, i.e., by connecting stubs of vertices.

    :param degree_seq: the degree sequence of a graph
    :return: A set of tuples, representing the edges.
    """
    def pick_stub():
        explored = set(range(len(degree_seq)))
        # eliminate all that are zero, and pick one
        # create new list containing indices
        non_zero_stubs = [i for i, d in enumerate(degree_seq) if d > 0]

        if len(non_zero_stubs) == 0: raise Exception("Something went wrong")

        # pick a random index of a list
        random_index = np.random.randint(low=0, high=len(non_zero_stubs))

        return non_zero_stubs[random_index]

    d_m = sum(degree_seq)
    edges = []
    while d_m > 0:
        # pick a two random integers
        # denoting id of stub
        # end connect them if they are not zero
        f_stub, s_stub = pick_stub(), pick_stub()
        d_m -= 2
        # basically, vertices f_stub, s_stub are connected
        degree_seq[f_stub] -= 1
        degree_seq[s_stub] -= 1
        edges.append((f_stub, s_stub))

    return edges


def irregular_edge_count(edges):
    """
    Computes ratio of multiedges and loops and simple edges

    :param edges: A list of tuples representing the set of edges of a graph.
    :return: The ratio described above.
    """
    unique_edges = set()
    loop_counter, multi_edge_cnt = 0, 0
    for e in edges:
        u, v = e
        # check if it is a loop
        if u == v: loop_counter += 1

        # check if it is multiedge
        if (u, v) in unique_edges or (v, u) in unique_edges: multi_edge_cnt += 1
        else: unique_edges.add(e)

    return float(loop_counter + multi_edge_cnt) / float(len(edges))

