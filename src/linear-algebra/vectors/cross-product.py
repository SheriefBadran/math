import numpy as np

u = np.array([1, 2, -2])
v = np.array([3, 0, 1])

# u x v
w = np.cross(u, v)

print('cross product vector perpendicular to u and v: ', w)

# If u and w are vectors in 3-space, then let's confirm that u x v is orthogonal to u 
# u • (u x v) = 0

print('u • (u x v) = 0: ', u.dot(np.cross(u, v)) == 0)

# Implementation of cross product function using cross product formula
def vector_cross_product(u: np.ndarray, v:np.ndarray) -> np.ndarray :
 
     if not isinstance(u, np.ndarray) or not isinstance(v, np.ndarray):
        raise TypeError('Expected array to be an np.ndarray')
     
     if u.size != 3 or v.size != 3:
         raise ValueError("The vector has to be a vector in R3, with 3 components/elements")
     
     # Cross product formula
     return np.array([u[1]*v[2] - u[2]*v[1], u[2]*v[0] - u[0]*v[2], u[0]*v[1] - u[1]*v[0]])

print('cross product vector calculated with vector_cross_product function: ', vector_cross_product(u, v))