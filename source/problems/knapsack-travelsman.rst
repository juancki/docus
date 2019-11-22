=============================================
Knapsack and Travel Salesman Combined Problem
=============================================

This problem comes out of simply adding the restrictions of two of the most famous optimization problems: Knapsack problem and the Travel Salesman problem.


Knapsack problem
----------------
There are items that we can select, each one with a value and some weight. The knapsack can only carry certain weight, known as capcity, otherwise will break.
The problem is stated as which items do we select in orde to maximize the value of the things that we can put inside of our knapsack.

The number of items to carry is not bounded, only the weight it can support. The first approximation to a solution might be to put the things with most value first. However, this does not lead to general optimal solution for this problem.

The complexity of the problem is that it is necessary to search for (almost) all combinations in order to solve the problem which has a great computational cost. Said with more technical words the problem is NP-hard, it can not be solved in polynomial time.


Travel Salesman Problem
-----------------------
This problems is about distances rather than weights. In this case we have a set of locations that we want to visit scattered over a space. All places have to be visited. What we want to minimize is the distance traveled, and thus save time and fuel, because we care about our employees and climate change.

Travel Salesmane representation problem
.......................................
**Graphs** :The actual positions of the locations is not relevant but the distance between them is. The problem is usually presented with a graph which vertexes are the locations and the edges are the distance from one vertex to the other.

**Matricial** :It can also be represented with a NxN matrix where N is the number of elements. The element :math:`a_{ij}` is the distance from the location :math:`l_i` to :math:`l_j`. If you can go and come from any two locations, the graph will be undirected and the matrix symetric. 


The Problem
===========






