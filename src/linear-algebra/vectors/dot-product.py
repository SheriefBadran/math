import numpy as np

# Consider the vectors u = (2, -1, 1) and v = (1, 1, 2). Find u • v and determine the angel betwen u and v

u = np.array([2, -1, 1])
v = np.array([1, 1, 2])

dot_uv = u.dot(v)

print('Dot prodcut of u and v: ', dot_uv)

norm_u = np.linalg.norm(u)
norm_v = np.linalg.norm(v)

print("norm_a: ", norm_u)
print("norm_b: ", norm_v)

# Calculate the angle between the vectors u and v

cos_theta = dot_uv/(norm_u * norm_v)
theta = np.arccos(cos_theta)

# Since arccos returns the angle theta in radians, we rater express the answer in terms of pi
theta_in_pi = theta/np.pi

print("angle between u and v: ", theta_in_pi)





