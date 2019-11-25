
================================================
Knapsack and Travel Salesman Combined Problem II
================================================

Breath First (recursive solution)
---------------------------------
This a first recursive solution to the optimization problem.

At any given time, the state of a wanna-be solution can be described with the following variables:

- Current location :math:`L`.
- Distance traveled :math:`d`.
- Current weight in the knapsack :math:`w`.
- To-do list, list of items that have to be picked-up :math:`T`.

.. code-block:: python

    def search(self):
        self.PQ = PriorityQueue()   # incomplete paths
        tree = Tree(self.world)
        self.paths= []              # complete paths
        self.PQ.put((tree,tree.parent,0,0),0)

        while not self.PQ.empty():
            T,node,d,w= self.PQ.get()
            result = self.add_to_tree(T,node,d,w)
            if result is not None: return

Base Case
---------
We arrive to the base case when the picker has no other place to go.  

.. code-block:: python

        # BASE CASE 
        if len(possible_transitions) == 0 and e.element is self.world.O :
            not_accessible.reverse()
            self.add_solution_to_paths(not_accessible,d)
            return

Recursive Case
--------------
If the picker has more places to go, the search has to continue.
The elements that are achivable from the current place,``t_possible`` have to be added to the PQ updating the distance  

.. code-block:: python

        # RECURSIVE CASE
        for t in t_possible:
            N = Node(t,e)
            e.child.append(N) # Added to the tree
            new_d = d+World.dist(e.element,t)
            new_w = w+t.el.w
            self.PQ.put((T,N,new_d,new_w),new_d)

        if e.element is not self.world.O:
            t = self.world.O
            N = Node(t,e)
            e.child.append(N) # Added to the tree
            new_d = d+World.dist(e.element,t)
            new_w = 0
            self.PQ.put((T,N,new_d,new_w),new_d)

