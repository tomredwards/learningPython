from scipy import constants

# For the optimization example
from scipy.optimize import minimize_scalar

# For the sparse data examples
import numpy as np
from scipy.sparse import csr_matrix

# For the Graph examples
from scipy.sparse.csgraph import connected_components, dijkstra


# SciPy has various constants defined
print(constants.liter)
print(constants.pi)


# NumPy is capable of finding roots for polynomials and linear equations, but it can not find roots for
# non-linear equations.  SciPy can find the root of non-linear equations using the Optimize package
def objective_function(x):
    return 3 * x ** 4 - 2 * x + 1


res = minimize_scalar(objective_function)
print(res)
print("\n\n")


# Dealing with sparse data ####################
arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
print("Sparse version of the array is:")
print(csr_matrix(arr))
# A two-dimensional array
d2_arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print(csr_matrix(d2_arr).data)
print(csr_matrix(d2_arr).count_nonzero())
mat = csr_matrix(d2_arr)
mat.eliminate_zeros()
print(mat)


# Graphs in SciPy ##########################
print("Playing with graphs in SciPy")
arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)
print(newarr)

print("Connected components: ", connected_components(newarr))
print("dijkstra shortest path: ", dijkstra(newarr, return_predecessors=True, indices=0))

