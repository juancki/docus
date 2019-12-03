=================================================
Knapsack and Travel Salesman Combined Problem III
=================================================

HEURISTIC SOLUTION (recursive solution)
---------------------------------------
This suboptimal solution serves as a test on the effects in the order of computations to better understand the computational burden of this project.
This is a better recursive solution to find a suboptimal solution to this problem problem that takes into account the structure of the problem when searching for solutions.

In the previous case with Breath First (BF), when the optimal solution has distance :math:`D` it is required that every branch in the Priority Queue (PQ) has at least cost :math:`D`. This is the major disadvantage of BF for the resolution of this problem because the number of branches increases exponentially in the very first interectactions.

In order to avoid having to compute all branches at the same pace, we need the algorithm to diferentiate between good and bad. This is where the heuristics brights. However, the heuristic function has to be defined and is not reusable from problem to problem. 

In this case, the heuristic function is a reinterpretation of the optimization problem. Due to the fact that the total number elements to pick up is the same, the ratio distance to #elements will be minimized when the distance is minimized at the end.

.. code-block:: python

        def heuristics(path,path_distance):
            return path_distance/len(path)

Where the ``path`` is the list of elements visited without the times that the picker has passed to Origin. And the ``path_distance`` is the distance traveled.

Similarly to the BF solution, this heuristic approximation keeps track of the branches with a Priority Queue (PQ), in this case, on the heuristics function. Then, when a branch is pop'ed from the PQ is the one that has traveled the least distance to #elements ratio. From that branch, all possible transitions are obtained and added to queue with their respective heuristics.

The constraints are also included as in the BF solution. The main change is the order at wich the braches are pop'ed from the PQ.


OPTIMUM
-------
The code as expressed above does not accomplish the optimum, but rather a suboptimum that is the path that has the best ratio distance to nodes until N-1.

Unfortunately for this approach, it is necessary to finish all the paths to guarantee that a solution is the best.

A* Algorithm
------------

Conditions on the heuristic function for A*....


.. code-block:: python

        def pq_index(path_distance,not_accessed):
                heuristic = len(not_accessed)
                cost = path_distance
                return cost + heuristic

