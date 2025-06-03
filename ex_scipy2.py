import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
from scipy import io


arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(connected_components(newarr))
#Find all of the connected components with the connected_components() method.

"""  
For a graph like this, with elements A, B and C, the connections are:

A & B are connected with weight 1.

A & C are connected with weight 2.

C & B is not connected.
      A B C
   A:[0 1 2]  
   B:[1 0 0]
   C:[2 0 0]"""

#dijkstra method to find the shortest path in a graph from one element to another.
"""It takes following arguments:

return_predecessors: boolean (True to return whole path of traversal otherwise False).
indices: index of the element to return all paths from that element only.
limit: max weight of path."""


arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(dijkstra(newarr, return_predecessors=True, indices=0))



arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])

# Export:
#savemat() function allows us to export data in Matlab format.
print(arr)
io.savemat('arr.mat', {"vec": arr})

# Import:
#The loadmat() function allows us to import data from a Matlab file.
mydata = io.loadmat('arr.mat')

print(mydata)

# We can see that the array originally was 1D, but on extraction it has increased one dimension.

#In order to resolve this we can pass an additional argument squeeze_me=True:

mydata = io.loadmat('arr.mat', squeeze_me=True)

print(mydata['vec'])