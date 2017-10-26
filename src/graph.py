""" CR15 graph library """
from collections import deque
import math
class Graph(object):

    def __init__(self, graph_dict={}):
        """ initializes a graph object """
        self.__graph_dict = graph_dict

    def vertices(self):
        """
        :returns: the vertices of a graph
        """
        return list(self.__graph_dict.keys())

    def number_of_vertices(self):
        """
        :return: returns the number of vertices
        """
        return len(self.__graph_dict.keys())

    def number_of_edges(self):
        """
        :return: returns the number of edges
        """
        return len(self.edges())

    def edges(self):
        """
        :return: a list of tuples representing the edges of the graph
        """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If vertex is not in self.__graph_dict, a key "vertex" with an empty
        list as a value is added to the dictionary. Otherwise nothing has to be 
        done.
        :return: True if the vertex is not present in the graph, otherwise false."""

        if vertex not in self.__graph_dict.keys():
            self.__graph_dict[vertex] = []
            return True
        else:
            return False

    def is_vertex_present(self, vertex):
        """Checks if the vertex is already created.
        Returns True if it is otherwise False"""
        if vertex in self.__graph_dict.keys():
            return True
        else:
            return False

    def in_neighbourhood(self, u, v):
        """
        :param u: a vertex of the graph
        :param v: a vertex of the graph
        :return: Returns True if v is in the neighborhood of u.
        It raises KeyError if u is not present in the graph.
        """
        if u not in self.vertices():
            raise KeyError("Vertex is not present in the graph")

        u_neighbors = self.get_neighbors(u)
        return v in u_neighbors

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list. No loops or 
        multiple edges.
        :return: Returns true if edge is not present, otherwise false."""

        u, v = edge
        return_type = False

        if not self.is_vertex_present(u):
            self.add_vertex(u)

        if not self.is_vertex_present(v):
            self.add_vertex(v)

        if v not in self.__graph_dict[u]:
            return_type = True
            self.__graph_dict[u].append(v)

        if u not in self.__graph_dict[v]:
            self.__graph_dict[v].append(u)

        return return_type

    def add_edges(self, edges):
        """
        Adds a list of edges to graph
        :param edges: a list of edges to be added
        :return: void
        """
        for edge in edges:
            self.add_edge(edge)

    def __generate_edges(self):
        """ A static method generating the edges of the graph "graph". Edges 
        are represented as sets two vertices, with no loops.
        :return: a list of tuples representing the edges
        """
        edges = []
        for u in self.__graph_dict.keys():
            for v in self.__graph_dict[u]:
                if (u, v) not in edges and (v, u) not in edges:
                    edges.append((u, v))
        return edges

    def vertex_degree(self, vertex):
        """
        Returns the degree of the vertex
        :param vertex: vertex for which degree is computed
        :return: return the degree if the vertex is present, otherwise raises keyerror
        """
        if self.is_vertex_present(vertex):
            return len(self.__graph_dict[vertex])
        else:
            raise KeyError("Vertex is not in the graph")

    def vertices_degree_list(self):
        """
        :return: returns a list of degrees of vertices
        """
        degrees = [self.vertex_degree(u) for u in self.vertices()]

        return degrees


    def find_isolated_vertices(self):
        """
        :return:a list of vertices of degree 0.
        """
        isolated_vertices = [u for u in self.vertices() if self.vertex_degree(u) == 0]

        return isolated_vertices

    def density(self):
        """
        Density is ratio of number of edges and number of edges that
        complete graph has with the same number of vertices.
        :return: returns the density of the graph
        """

        num_of_edges = self.number_of_edges()
        num_of_vertices = self.number_of_vertices()

        poss_num_of_edges = num_of_vertices * (num_of_vertices - 1) / 2

        if poss_num_of_edges == 0:
            return 0

        return float(num_of_edges) / float(poss_num_of_edges)

    def degree_sequence(self):
        """
        Degree sequence is a list of all degrees in non-increasing order
        :return: a degree sequence of the graph
        """

        degree_seq = sorted(self.vertices_degree_list(), reverse=True)
        return degree_seq

    def erdos_gallai(self):
        """
        Erdos Gallai theorem states that a non-increasing
        sequence of n numbers d_i is a degree sequence of a simple graph
        if and only if the sum of sequence is even and the condition
        sum_{i=1}^{k}{d_i} <= k(k-1) + sum_{i=k+1}^n min(d_i, k) for all k
        This can be implemented in time O(nlogn). However, the current implementation
        requires O(n^2) time.
        :return: True if the degree sequence satisfies both conditions and False otherwise
        """

        degree_seq = self.degree_sequence()

        # first condition is satisfied by default

        # second condition
        num_vertices = self.number_of_vertices()

        def compute_right_sum(k):
            elements = [min(d, k) for d in degree_seq[k+1:]]
            return sum(elements)

        left_sum = 0
        for k in range(num_vertices):
            # compute left and right sum
            left_sum = left_sum + degree_seq[k]
            right_sum = compute_right_sum(k)

            if left_sum > k*(k-1) + right_sum:
                return False

        return True

    def global_clustering_coefficient(self):
        """
        Global clustering coefficient is the ratio of number of triangles and
        number of connected triplets of vertices
        :return: clustering coefficient of the graph
        """

        num_closed_triplets = 0
        num_conn_triplets = 0

        for u in self.vertices():
            # center it at vertex u
            tmp_conn_trplets = 0
            tmp_closed_triplets = 0

            # check if there is a closed or conn
            # triplet centered at u
            u_neighbors = self.get_neighbors(u)
            for i, v in enumerate(u_neighbors):
                for w in u_neighbors[i+1:]:
                    if self.in_neighbourhood(v, w):
                        # this is a closed triplet
                        tmp_closed_triplets += 1

                    num_conn_triplets += 1

            num_closed_triplets += tmp_closed_triplets
            num_conn_triplets += tmp_conn_trplets


        if num_conn_triplets == 0:
            return 0
        print("conn = %d, closed = %d" % (num_conn_triplets, num_closed_triplets))
        return float(num_closed_triplets) / float(num_conn_triplets)

    def get_neighbors(self, u):
        """
        :param u: vertex in the graph
        :return: a list of neighbors of u
        """

        if not self.is_vertex_present(u):
            raise KeyError("Vertex is not in the graph")
        else:
            return self.__graph_dict[u]

    def connected_components(self):
        """
        Computes connected components
        :return: a list of lists, each containing vertices from the same conn component
        """
        n = self.number_of_vertices()
        all_comps = [] #

        # keep all unvistied nodes in a set
        all_nodes = set(self.vertices())

        while len(all_nodes) > 0: # while there is an unvisited node
            u = all_nodes.pop()

            curr_component = {u} # all nodes belonging to this component
            bfs_queue = {u} # use set (our favourite data struct) as a bfs queue

            while len(bfs_queue) > 0: # while there is a node in the queue
                u = bfs_queue.pop()

                # get all my neighbors
                # keep it in a set in order to make operations faster
                u_neighbors = set(self.get_neighbors(u))

                # remove those vertices I already saw
                u_neighbors.difference_update(curr_component)

                # update current component
                curr_component.update(u_neighbors)

                # update set of visited nodes
                all_nodes.difference_update(u_neighbors)

                # update queue
                bfs_queue.update(u_neighbors)

            all_comps.append(list(curr_component))

        return all_comps

    def connected_component(self):
        """
        Computes the number of connected components and
        the size of each componenent
        :return: a pair: thi first entry is the number of components, the second
        is a list constaining sizes of components
        """
        components = self.connected_components()
        number_of_comps = len(components)

        sizes = []
        for i, comp in enumerate(components):
            sizes.append(len(comp))

        return number_of_comps, sizes


    def shortest_path(self, u=None, v=None):
        """
        Computes the shortest path between u and v.
        If both of them are None, then computes the shorthest path
        between all pair of vertices.
        If u is not None and v is None, then it computes the shortest path
        between u and all other vertices.
        Finally, if both of them are not None, it computes the shorthest path
        between u and v.
        :param u: the source vertex
        :param v: the end vertex
        :return: the shortest path
        """
        # now we need a real queue :(
        if u is None and v is None:
            return {u: self.shortest_path(u=u) for u in self.vertices()}

        dist, arg_u, arg_v = {}, u, v

        u = u if u is not None else v  # love python
        queue = deque([u])

        # distance to me is 0
        dist[u] = 0

        while len(queue) > 0:
            # take the best so far
            u = queue.pop()

            u_neighbors = self.get_neighbors(u)

            updated = {v: dist[u] + 1 for v in u_neighbors if v not in dist.keys()}

            # append the queue
            queue.extend(updated.keys())

            # update distances
            dist.update(updated)

        # nodes which are not in the list are not in the
        # same component as u

        non_reachable = {v: int("inf") for v in self.vertices() if v not in dist.keys()}

        # update for non_reachable
        dist.update(non_reachable)

        if arg_u is not None and arg_v is not None:
            return dist[v]
        else:
            return dist

    def diameter(self):
        """
        Computes the diameter of the graph
        :return: The maximum of distances between any pair
        of nodes or infinity if the graph is not connected
        """
        dist = self.shortest_path()

        # a temporary function to compute the largest distance
        # starting at u
        def u_diameter(u):
            values = dist[u].values()
            return 0 if len(values) == 0 else max(values)

        # compute the largest distances from every vertex
        comp_diams = [u_diameter(u) for u in self.vertices()]

        # finally compute the diameter
        diam = 0 if len(comp_diams) == 0 else max(comp_diams)

        return diam

    def biggest_component_diameter(self):
        """
        :return: the diameter of the biggest component
        """

        all_components = self.connected_components()

        # get components and their sizes
        component_sizes = [(len(comp), i) for i, comp in enumerate(all_components)]
        if len(component_sizes) == 0:
            return 0

        size_of_largest, idx_largest = max(component_sizes)

        # now it is guaranteed that there is at least one vertex
        dist = self.shortest_path()

        # map every vertex from the largest component to
        # largest distance starting at that vertex

        def u_diameter(u):
            values = [val for val in dist[u].values() if not math.isinf(val)]
            return 0 if len(values) == 0 else max(values)

        diam_candidates = [u_diameter(u) for u in all_components[idx_largest]]
        return max(diam_candidates)

    def spanning_tree(self):
        """
        Computes the spanning tree of the graph using Kruskal algorithm
        and union - find. Complexity: O(mlog*(n))
        :return: a list of tuples representing edges of the tree
        """
        parent_and_rank = {node:[node,0] for node in self.vertices()}
        s_tree = [] # edges of resulting tree
        def find_parent(x):
            if parent_and_rank[x][0] != x:
                parent_and_rank[x] = find_parent(parent_and_rank[x][0])
            return parent_and_rank[x]

        for u,v in self.edges():
            uroot = find_parent(u)[0]
            vroot = find_parent(v)[0]

            if uroot == vroot: # this edge create a cycle
                continue

            # otherwise, add this edge to the tree and join components
            s_tree.append((u, v))

            uroot_rank = parent_and_rank[uroot][1]
            vroot_rank = parent_and_rank[vroot][1]

            if uroot_rank > vroot_rank:
                parent_and_rank[vroot] = [uroot, parent_and_rank[uroot][1]]
            elif uroot_rank < vroot_rank:
                parent_and_rank[uroot] = [vroot, parent_and_rank[vroot][1]]
            else:
                parent_and_rank[vroot] = [uroot, parent_and_rank[uroot][1]]
                parent_and_rank[uroot][1] += 1

        return s_tree



if __name__ == "__main__":

    G = {
      "a": ["c", "d", "g"],
      "b": ["c", "f"],
      "c": ["a", "b", "d", "f"],
      "d": ["a", "c", "e", "g"],
      "e": ["d"],
      "f": ["b", "c"],
      "g": ["a", "d"]
    }
    graph = Graph(G)
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())
    print("Connected components")
    print(graph.connected_components())
