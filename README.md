# Social Network Analysis - Pagerank Calculation
Write a function called pagerank to calculate the PageRank of all nodes of a graph.  

Input:  

1. G - Networkx Directed Graph Object 
2. max_iter - Number of Iterations (should have some default value) 
3. d - damping parameter (should have some default value)
4. has_weight - boolean to be set if using a weighted graph (should have some default value) 

Output: A dict where key is a node and values is the pagerank value  

Note:  The function should Create 

1. Transiston Matrix, A 
2. Create initial vector, v0 
3. Write update equation, Av0 = v1 
4. Write convergence condition, number of iterations or no change in page rank values 
5. Iteratively update the PageRank values until convergence condition has been reached
