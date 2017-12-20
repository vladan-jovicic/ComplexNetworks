Testing implemented algorithms
==============================

The project also contains a different test used for testing the correctnes of implemented algorithms.
The tests are written using python *unittest* module.

In general, there are two tests:
- **simple tests** (*GraphTest.py*): testing the algorithms on a small simple graph where parameters are known in advance
- **networkx tests** (*NetworkxTest.py*): comparing the results of algorithms with networkx results.

Simple tests
------------

In order to run this tests, navigate to the **test** folder and execute the following:

.. code:: ipython2

    python -m unittest -v GraphTest

It will output results for all the tests. Here is an example:

.. parsed-literal::

    test_clustering (GraphTest.GraphTest) ... ok
    test_degree_seq (GraphTest.GraphTest) ... ok
    test_density (GraphTest.GraphTest) ... ok
    test_diameter (GraphTest.GraphTest) ... ok
    test_erdos_gallai (GraphTest.GraphTest) ... ok
    test_isolated_vertices (GraphTest.GraphTest) ... ok
    test_shortest_path_uv (GraphTest.GraphTest) ... ok
    test_spanning_tree (GraphTest.GraphTest) ... ok
    test_vertex_degree (GraphTest.GraphTest) ... ok

    Ran 9 tests in 0.001s

    OK

Networkx tests
--------------

As already stated, these tests are used to compare results with *NetworkX* module results.
So far, only a few tests are implemented.

These tests can be run on different graphs provided that the format is the same as in the project description.
To change the input graph, set the variable **filename** in *NetworkxTest.py/GraphTest/setUpClass* equal to the pat of file where
graph description is provided.

We will test it on *zachary_connected.txt* example.
Here is the output:

.. code:: ipython2

    python -m unittest -v NetworkxTest

.. parsed-literal::

    test_density (NetworkxTest.GraphTest) ... ok
    test_diameter (NetworkxTest.GraphTest) ... ok
    test_erdos_gallai (NetworkxTest.GraphTest) ... ok
    test_isolated_vertices (NetworkxTest.GraphTest) ... ok
    test_shortest_path_uv (NetworkxTest.GraphTest) ... ok
    test_vertex_degree (NetworkxTest.GraphTest) ... ok

    Ran 6 tests in 0.011s

    OK

These tests can be also used to compare time used by the implemented algorithms and *NetworkX* module.
This feature is not available publicly at the moment.