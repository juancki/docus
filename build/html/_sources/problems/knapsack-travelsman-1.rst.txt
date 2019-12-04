================================================
Knapsack and Travel Salesman Combined Problem II
================================================


Breath First 
-------------
This a first recursive solution to the optimization problem. With Breath First we are going search find the solution in the decision tree.

The algorithm keeps track of all the branches at the same time with a Priority Queue (PQ) based on the total distance. At any time, the branch with least traveled distance is pop'ed from the PQ and is analyzed. From that branch, all possible transitions are obtained and added to queue with their respective cost.

At any given time, the state of a wanna-be solution can be described with the following variables:

- Current location :math:`L`.
- Distance traveled :math:`d`.
- Current weight in the knapsack :math:`w`.
- To-do list, list of items that have to be picked-up :math:`T`.

The PQ is initialized with the top of tree which is the Origin.
Then, the Breath First will keep on searching (``add_to_tree``)until the a solution is found.

.. code-block:: python

    def search(self):
        self.PQ = PriorityQueue()   # incomplete paths
        tree = Tree(self.world)
        self.paths= []              # complete paths
        self.PQ.put((tree,tree.parent,0,0),0)

        while not self.PQ.empty():
            T,node,d,w= self.PQ.get()
            result = self.add_to_tree(T,node,d,w)
            if result is not None: 
                return # comment this line to avoid exhaustive search

``add_to_tree`` and  Base Case
______________________________
The locations that have been passed by in any given branch is the list of parent nodes of the tree from the current node to the top.
The possible transitions from there are those that have not been visited and also, allowed by the capacity constraint.

We arrive to the base case when the picker has no more places to visit and is on the Origin. In that case, solution will be reported to the main loop where, if desired, and the search will be finished.

.. code-block:: python

    def add_to_tree(self,T,e,d,w):
        p = e.parent
        not_accessible = [e.element]
        while p is not None:
            not_accessible.append(p.element)
            p = p.parent

        t_zero_weight = [q for q in self.world.elements if q not in not_accessible]

        # Posible transitions to other locations
        t_possible = [q for q in t_zero_weight if (q.el.w + w) <= self.ks.max_weight]

        # BASE CASE 
        if len(possible_transitions) == 0 and e.element is self.world.O :
            not_accessible.reverse()
            self.add_solution_to_paths(not_accessible,d)
            return 'solution found'

        # Continues with the recursive cases

Recursive Case
--------------
If the picker has more places to go or it is not on the Origin, the search has to continue.

Two transition cases are separated: 1) From any location to an item and 2) From an item to the Origin.

1) From any location to an item.

        The elements that are achivable from the current place, ``t_possible`` have to be added to the PQ with the status:
        
        - ``new_d`` is the distance traveled until ``e`` plus the distance from there to each possible transtion.
        - ``new_w`` is the cumulative weight in the knapsack once the picker arrives to each possible transition.
        - ``N``  is the node from the decision tree whose parent is ``e`` and represent the transition from ``e`` to ``t`` in that branch.
        - The information about the to-do list and the traveled is inherent in the tree ``T``.

2) From an item to the Origin.

        In this case, the picker can go to the Origin if is not in the Origin. The new added cases to the PQ will have:
        
        - ``new_w`` is simply zero, because the picker unpacks the knapsack on the Origin.
        - ``new_d``, calculated in the same way as before, is the distance traveled until ``e`` plus the distance to the Origin.
        - ``N``  is the node from the decision tree whose parent is ``e`` and represent the transition from ``e`` to ``t`` in this case the Origin.
        - The information about the to-do list and the traveled is inherent in the tree ``T``.

The code is not actually recursive, but if it was written recursivelly, this would be the recursive cases.

.. code-block:: python

        # RECURSIVE CASE
        for t in t_possible:            # For every possible transition
            N = Node(t,e)
            e.child.append(N)           # Add transition to the tree
            new_d = d+World.dist(e.element,t)
            new_w = w+t.el.w
            self.PQ.put((T,N,new_d,new_w),new_d)

        if e.element is not self.world.O:
            t = self.world.O
            N = Node(t,e)
            e.child.append(N)           
            new_d = d+World.dist(e.element,t)
            new_w = 0                   # knapsack will be emptied.
            self.PQ.put((T,N,new_d,new_w),new_d)



OPTIMUM
-------
The code as expressed above does not accomplish the optimum, but it almost does.
In order to obtain the optimum, once the first solution has been found, the algorithm has to check if the branches pop'ed from the PQ have greater traveled distance than the solutions found. When this happens, the solution is to get the least from the already obtained solutions.


