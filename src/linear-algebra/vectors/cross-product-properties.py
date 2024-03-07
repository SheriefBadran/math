import sympy as sp

# Prove that u • (u x v) = 0 and v • (u x v) = 0

a, b, c = sp.symbols('u1 u2 u3')
d, e, f = sp.symbols('v1 v2 v3')

# Two vectors u and v in R3
u = sp.Matrix([a, b, c])
v = sp.Matrix([d, e, f])

print('u • (u x v) = 0: ', sp.simplify(u.dot(u.cross(v))) == 0)
print('v • (u x v) = 0: ', sp.simplify(v.dot(u.cross(v))) == 0)

# Prove the theorem u x (v x w) = (u • w)v - (u • v)w (Relationship between cross and dot products)

# Let's introduce vector w
g, h, i = sp.symbols('w1, w2, w3')
w = sp.Matrix([g, h, i])

lhs = sp.simplify(u.cross(v.cross(w)))
rhs = sp.simplify((u.dot(w) * v) - (u.dot(v) * w))
print('u x (v x w) = (u • w)v - (u • v)w: ', lhs.equals(rhs))

# Prove the theorem (u x v) x w = (u • w)v - (v • w)u (Relationship between cross and dot products)
# Let's apply u x v = - (v x u) to the result of theorem u x (v x w) = (u • v)v - (u • v)w
expression_A = u.cross(v).cross(w)

# Using the theorem u x (v x w) = (u • w)v - (u • v)w, proved above, expression_B = expression_C
expression_B = (-w).cross(u.cross(v))
expression_C = (-w).dot(v) * u - (-w).dot(u) * v

# Simplifying expression_C further, leads us to expression_F:
expression_D = -(w.dot(v)) * u + w.dot(u) * v
expression_E = -(v.dot(w)) * u + u.dot(w) * v
expression_F = u.dot(w) * v - (v.dot(w)) * u

# List all valid expressions for the theorem
expressions = [expression_A, expression_B, expression_C, expression_D, expression_E, expression_F]

# Check that each expression is equal to expressionA
# If all expressions are equal to expression_A, it is proved that expression_A = expression_F
all_equal = all(expression.equals(expressions[0]) for expression in expressions[1:])

print('(u x v) x w = (u • w)v - (v • w)u: ', all_equal)

# Prove Lagrange's identity ||u x v||^2 = ||u||^2 * ||v||^2 - (u • v)^2
uv_cross = u.cross(v)
left_hand_side = uv_cross[0]**2 + uv_cross[1]**2 + uv_cross[2]**2
right_hand_side = (u[0]**2 + u[1]**2 + u[2]**2) * (v[0]**2 + v[1]**2 + v[2]**2) - u.dot(v)**2

# Let's expand both expressions in order to visually demonstrate the equality
print('left hand side: ', left_hand_side.expand())
print('right hand side: ', right_hand_side.expand())

result = left_hand_side.equals(right_hand_side)

print('||u x v||^2 = ||u||^2 * ||v||^2 - (u • v)^2 :', result)