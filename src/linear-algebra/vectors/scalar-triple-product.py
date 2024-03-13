import sympy as sp

# If u, v and w are vectors in 3-space, then u • (v x w) is called the scalar triple product of u, v and w.
# If A is 3 x 3 matrix made up the vectors of u, v and w. Prove the scalar triple product formula: u • (v x w) = det(A)

u1, u2, u3, v1, v2, v3, w1, w2, w3 = sp.symbols('u1:4 v1:4 w1:4')

u = sp.Matrix([u1, u2, u3])
v = sp.Matrix([v1, v2, v3])
w = sp.Matrix([w1, w2, w3])

# Calculate the scalar triple product
scalar_triple_product = u.dot(v.cross(w))

# Let's vertically stack the vectors as row vectors in matrix A (they are column vectors by default)
A = sp.Matrix.vstack(u.T, v.T, w.T)

# Proving the scalar triple product formula:
print('u • (v x w) = det(A): ', sp.expand(scalar_triple_product) == A.det())