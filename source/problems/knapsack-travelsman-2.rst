=================================================
Knapsack and Travel Salesman Combined Problem III
=================================================

A START (A*) (recursive solution)
---------------------------------
A* is a path search algorithm used in Navigation and Robotics to travel through graphs. It is a 
This is a better recursive solution to the optimization problem that takes into account the structure of the problem when searchin for solutions.

In the previous case with Breath First, when the optimal solution has distance :math:`D` it is required that every branch in the decision tree has at least cost :math:`D`. This is the major disadvantage of this technique to this problem because the number of branches increases exponentially in the very first interectactions.

In order to avoid having to compute all branches at the same pace, we need the algorithm to diferentiate between good and bad. This is where the A* algorithm heuristic brights. However, the heuristic function has to be defined and is not reusable from problem to problem. 

In this case, the heuristic function is a reinterpretation of the optimization problem. Due to the fact that the total number elements to visit is the same, the ratio distance to #elements will be minimized when the distance is minimized.

.. code-block:: python

        def heuristics(path,path_distance):
            return path_distance/len(path)

Where the ``path`` is the list of elements visited without the Origin. And the ``path_distance`` is the distance traveled.

Similarly to the Breath First solution, A* keeps track of the branches with a Priority Queue (PQ) based, in this case, on the heuristics. Then, when a branch is pop'ed from the PQ is the one that has traveled the least distance to #elements ratio. From that branch, all possible transitions are obtained and added to queue with their respective heuristics.



OPTIMUM
-------
The code as expressed above does not accomplish the optimum, but it almost does.
In order to obtain the optimum, the algorithm has to check if the branches pop'ed from the PQ have greater traveled distance than the solutions found. When this happens, the solution is to get the least from the already obtained solutions.
