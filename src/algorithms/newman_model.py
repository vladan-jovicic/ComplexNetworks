import sys, os, math
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def degree_sequence_regular(n, k):
    return [k] * n


def degree_sequence_lognormal(n, mu, sigma):

    degree_seq = np.random.normal(mu, sigma, size=n)
    return degree_seq


def configure_sequence(degree_seq):

    def pick_stub():
        while True:
            stub = np.random.randint(0, len(degree_seq))
            if degree_seq[stub] > 0:
                return stub

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
    unique_edges = set()
    loop_counter, multi_edge_cnt = 0, 0
    for e in edges:
        u, v = e
        # check if it is a loop
        if u == v: loop_counter += 1

        # check if it is multiedge
        if (u, v) in unique_edges or (v, u) in unique_edges:
            multi_edge_cnt += 1
        else: unique_edges.add(e)

    return (loop_counter + multi_edge_cnt) / len(edges)
