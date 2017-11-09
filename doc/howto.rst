
How to use implemented algorithms
=================================

Overview
--------

The project has the following structure:

-  *doc* contains documentation of the project
-  *src* contains all the source code

   -  *algorithms* contains different algorithms
   -  *test* contains modules for testing with unittest

-  *test\_data* contains test data
-  *tools* different tools (scripts) used for building and testing
-  *Notebooks* contains ipython notebooks which demonstrate usage

Importing *Graph* module
------------------------

Firstly, we will import the *Graph* module. We are in the folder
*Notebooks* so, we need to append the path.

.. code:: ipython2

    import sys, os
    # sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath('../src/'))))
    sys.path.append('../src/')
    import graph
    reload(graph)




.. parsed-literal::

    <module 'graph' from '../src/graph.pyc'>



We will check if the library is imported correctly by computing a few
parameters of empty graph.

.. code:: ipython2

    emptyG = graph.Graph()
    diam = emptyG.diameter()
    gcc = emptyG.global_clustering_coefficient()
    print("The diameter of empty graph: %d" % diam)
    print("The global cluster coeff of empty graph is: %f" % gcc)


.. parsed-literal::

    The diameter of empty graph: 0
    The global cluster coeff of empty graph is: 0.000000


Reading graph from a file
-------------------------

Now we will show how to read graph from a file and compute requested
parameters.

.. code:: ipython2

    path = '../test_data/'
    txt = ".txt"
    filenames = ['zachary_connected', 'graph_1000n_4000m', 'graph_100n_1000m']
    
    graphs = [] # store all three graph objects in a list
    for i, g_name in enumerate(filenames):
        g = graph.Graph({})
        g.read_from_file(filename=path+g_name+txt)
        graphs.append(g)
        
        
    results = []
    params = ["vertices", "edges", "density", "diameter", "clustering coef"]
    
    print("%d, %d" % (graphs[0].number_of_vertices(), graphs[0].number_of_edges()))
    print("%d, %d" % (graphs[1].number_of_vertices(), graphs[1].number_of_edges()))
    print("%d, %d" % (graphs[2].number_of_vertices(), graphs[2].number_of_edges()))



.. parsed-literal::

    33, 78
    1000, 3989
    100, 960


Computing requested parameters
------------------------------

We assume that the provided graphs are simple and thus multi edges in
the files are ignored. Since one of the graphs has 1000 vertices and
3989 edges, computation of diameter will take some time.

.. code:: ipython2

    # compute parameters
    for i, G in enumerate(graphs):
        temp_results = [G.number_of_vertices(), G.number_of_edges(),
                        G.density(), G.diameter(),
                        G.global_clustering_coefficient()
                       ]
        results.append(temp_results)

Now we will present the results in a table. Notice that package
*ipy\_table* is required.

.. code:: ipython2

    from ipy_table import *
    
    
    dictList = []
    data_str = "dataset"
    
    # convert the dictionary to a list
    for i in range(len(results)+1):
        if i == 0:
            dictList.append([data_str] + [p for p in params])
        else:
            dictList.append([filenames[i-1]] + results[i-1])
        
    
    # create table with make_table
    make_table(dictList)
    
    set_column_style(0, width='100', bold=True, color='hsla(225, 80%, 94%, 1)')
    set_column_style(1, width='100')
    
    # render the table
    render()





.. raw:: html

    <table border="1" cellpadding="3" cellspacing="0"  style="border:black; border-collapse:collapse;"><tr><td  style="background-color:hsla(225, 80%, 94%, 1);border-left: 1px solid;border-right: 1px solid;border-top: 1px solid;border-bottom: 1px solid;width:100px;"><b>dataset</b></td><td  style="border-left: 1px solid;border-right: 1px solid;border-top: 1px solid;border-bottom: 1px solid;width:100px;">vertices</td><td  style="border-left: 1px solid;border-right: 1px solid;border-top: 1px solid;border-bottom: 1px solid;">edges</td><td  style="border-left: 1px solid;border-right: 1px solid;border-top: 1px solid;border-bottom: 1px solid;">density</td><td  style="border-left: 1px solid;border-right: 1px solid;border-top: 1px solid;border-bottom: 1px solid;">diameter</td><td  style="border-left: 1px solid;border-right: 1px solid;border-top: 1px solid;border-bottom: 1px solid;">clustering&nbsp;coef</td></tr><tr><td  style="background-color:hsla(225, 80%, 94%, 1);border-left: 1px solid;border-right: 1px solid;border-top: 1px solid;border-bottom: 1px solid;width:100px;"><b>zachary_connected</b></td><td  style="border-left: 1px solid;border-right: 1px solid;border-top: 1px solid;border-bottom: 1px solid;width:100px;">33</td><td  style="border-left: 1px solid;border-right: 1px solid;border-top: 1px solid;border-bottom: 1px solid;">78</td><td  style="border-left: 1px solid;border-right: 1px solid;border-top: 1px solid;border-bottom: 1px solid;">0.1477</td><td  style="border-left: 1px solid;border-right: 1px solid;border-top: 1px solid;border-bottom: 1px solid;">5</td><td  style="border-left: 1px solid;border-right: 1px solid;border-top: 1px solid;border-bottom: 1px solid;">0.1546</td></tr><tr><td  style="background-color:hsla(225, 80%, 94%, 1);border-left: 1px solid;border-right: 1px solid;border-top: 1px solid;border-bottom: 1px solid;width:100px;"><b>graph_1000n_4000m</b></td><td  style="border-left: 1px solid;border-right: 1px solid;border-top: 1px solid;border-bottom: 1px solid;width:100px;">1000</td><td  style="border-left: 1px solid;border-right: 1px solid;border-top: 1px solid;border-bottom: 1px solid;">3989</td><td  style="border-left: 1px solid;border-right: 1px solid;border-top: 1px solid;border-bottom: 1px solid;">0.0080</td><td  style="border-left: 1px solid;border-right: 1px solid;border-top: 1px solid;border-bottom: 1px solid;">6</td><td  style="border-left: 1px solid;border-right: 1px solid;border-top: 1px solid;border-bottom: 1px solid;">0.0070</td></tr><tr><td  style="background-color:hsla(225, 80%, 94%, 1);border-left: 1px solid;border-right: 1px solid;border-top: 1px solid;border-bottom: 1px solid;width:100px;"><b>graph_100n_1000m</b></td><td  style="border-left: 1px solid;border-right: 1px solid;border-top: 1px solid;border-bottom: 1px solid;width:100px;">100</td><td  style="border-left: 1px solid;border-right: 1px solid;border-top: 1px solid;border-bottom: 1px solid;">960</td><td  style="border-left: 1px solid;border-right: 1px solid;border-top: 1px solid;border-bottom: 1px solid;">0.1939</td><td  style="border-left: 1px solid;border-right: 1px solid;border-top: 1px solid;border-bottom: 1px solid;">3</td><td  style="border-left: 1px solid;border-right: 1px solid;border-top: 1px solid;border-bottom: 1px solid;">0.1928</td></tr></table>


