import numpy as np
import sys
sys.path.insert(0, '../')
import graph
import erdos_renyi as er


def barabasi_albert(N, m, g=None, n=None, p=None, seed=1):
    """
    Creates a random graph following Barabasi-Albert model.
    :param N: Number of vertices.
    :param m: Number of neighbors for every new node.
    :param g: A starting small network. If it is None,
    a small network is generated using erdos renyi model.
    :return: An instance of Graph representing the created graph.
    """

    rng = np.random.RandomState(seed)

    if g is None:
        p = rng.uniform(0, 1.0)
        n = rng.randint(0, 5)
        g = er.er_np(n, p)

    if N <= n:
        raise Exception("The total number of nodes"
                        "must be larger that the number of nodes"
                        "in the starting network")
    for u in range(n, N):
        g.add_vertex(u)

    degree_sum = 2*g.number_of_edges()
    all_vertices = range(N)

    for u in range(n, N):
        # construct probabilities
        degree_dist = np.array(g.vertices_degree_list(), dtype=np.float32)
        # note that it will not be connected to itself
        # since u does not belong to the support of our pmf
        probas = degree_dist / float(degree_sum)

        u_neighbors = rng.choice(all_vertices, m, False, probas)

        for v in u_neighbors:
            g.add_edge((u, v))
        degree_sum += 2*m

    return g








