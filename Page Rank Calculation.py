# -*- coding: utf-8 -*-

# Installing the networkx package
!pip install networkx

# Importing necessary packages
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Defining the graph and adding edges between the nodes in the graph
def create_toy_network():

  G = nx.DiGraph()
  edges = [('9','7'), ('8','7'), ('8','6'), ('8','5'), ('7','6'), ('7','5'), ('6','5'), ('6','4'), ('5','4'), ('4','3'), ('4','1'), ('8','7'), ('3','2'), ('3','1'), ('2','1')]
  G.add_edges_from(edges)
  return G

G = create_toy_network()

# Displaying the created graph with labels
nx.draw(G, with_labels = True)
plt.show()

# Creating a pagerank function to return each node of the graph along with its respective page rank value
# The definition inputs the required Graph, number of iterations to calculate the page rank over (max_iter), damping factor and if the graph has weights - True or False
def pagerank(G, max_iter=1000, d=0.85, has_weight=False):
  # Creating an empty dictionary for returning the required output
  page_rank_dict = {}
  # Transistion Matrix
  # Calculating the Total number of nodes in the graph(G)
  count = G.number_of_nodes()
  # Finding out the from and to nodes of directed edge. The results are sorted in a list based on ascending order of the node numbers for easier interpretability
  edges = list(sorted(G.out_edges(),reverse=False))
  # Checking if the Graph nodes have no edges between them then break else continue calculating their respective page ranks
  if(edges == []):
    print('The graph has no edges between its nodes')
  else:
    # Creating a number of nodes into number of nodes zero matrix
    trans = np.zeros([count,count], dtype=float)
    # Creating a adjacency matrix for a directed graph by assigning a 1 when the nodes in the respective column have a directed outgoing edge towards the respective row node
    n = 1
    for i in trans:
      for j in edges:
        if(j[1]==str(n)):
          i[int(j[0])-1] = 1
      n += 1

    # Summing up the individual column values of the created adjacency matrix
    cols_sum = trans.sum(axis=0)
  
    # Creating a transition matrix by dividing individual values in the adjacency matrix by the created sum of each column
    index = 0
    for i in trans:
      for j in cols_sum:
        if j != 0:
          i[index]= i[index]/j
        else:
          # Handling the column when it has only 0's using dangling factor, that is 
          i[index] = 1/count  
        index += 1
      index = 0
  
    A = np.round(trans,3)
  
    # Initial vector
    v0 = np.array([1/count] * count)

    #Iterate
    initial_iteration = 0
    vector = v0
    while initial_iteration < max_iter:
      #update equation
      v1 = vector
      vector = d*(A.dot(v1))+(1-d)/count
      initial_iteration+=1
      #convergence condition check - if the difference between the current and the previous page rank format is very very small that is 1.0e-5 then break
      if np.abs(v1 - vector).sum() <= 1.0e-5:
        break
    page_rank_dict = dict(zip(list(G.nodes()), list(vector)))
    return page_rank_dict

# Calling the pagerank Function
pagerank(G)
