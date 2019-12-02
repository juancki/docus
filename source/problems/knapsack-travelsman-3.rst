================================================
Knapsack and Travel Salesman Combined Problem IV
================================================

Until now, we have presented the problem, a way to find an optimum solution using Breath First and a suboptimal solution with a heuristic function. 
In this article we are going to focus on the combinations and permutations of the solutions to this problem.

- Intra-subpath permuation
- Inter-subpath permuation

Intra-Subpath permutation
-------------------------
First off we are going to define the **subpath**. A subpath is any combination of picked elements between consecutive passes through the Origin. The special part about a subpath is that it always starts and ends at the Origin with the knapsack emtpy.


.. code-block:: python

        # Distance matrix
        [[0.         9.75354174 4.87325056]
         [9.75354174 0.         5.07073511]
         [4.87325056 5.07073511 0.        ]]
        [
        # Weight and position
        A = Ew(E(weight=3),P(x=1.4943,y=1.6344)),
        B = Ew(E(weight=1),P(x=-7.4938,y=-2.1532)),
        C = Ew(E(weight=3),P(x=-3.2830,y=0.6719))]

        
=======  ===================
COST     PATH        
=======  ===================
20.6478  O->B->C->O->A->O   
20.6478  O->C->B->O->A->O   
20.6478  O->A->O->B->C->O   
20.6478  O->A->O->C->B->O   
26.4671  O->A->B->O->C->O   
26.4671  O->B->A->O->C->O   
26.4671  O->C->O->A->B->O   
26.4671  O->C->O->B->A->O   
26.7251  O->A->O->B->O->C->O
26.7251  O->A->O->C->O->B->O
26.7251  O->B->O->A->O->C->O
26.7251  O->B->O->C->O->A->O
26.7251  O->C->O->A->O->B->O
26.7251  O->C->O->B->O->A->O
=======  ===================


Inter-Subpath permutation
-------------------------
Moreover, the subpath in any path are conmutable as the total traveled distance is not modified.