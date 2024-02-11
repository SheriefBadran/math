import numpy as np
import math

# Consider the vectors u = (2, -1, 1) and v = (1, 1, 2). Find u • v and determine the angel betwen u and v

def calculate_vectors_angle(u: np.ndarray, v: np.ndarray) -> float :

    if not isinstance(u, np.ndarray) or not isinstance(v, np.ndarray):
        raise TypeError('Expected arr to be an np.ndarray')
    
    dot_uv = u.dot(v)
    norm_u = np.linalg.norm(u)
    norm_v = np.linalg.norm(v)
    
    cos_theta = dot_uv/(norm_u * norm_v)
    return np.arccos(cos_theta)

rad_angle_uv = calculate_vectors_angle(np.array([2, -1, 1]), np.array([1, 1, 2]))

# Since arccos returns the angle theta in radians, we rather express the answer in terms of pi
theta_in_pi = rad_angle_uv/np.pi

print("angle between u and v: ", theta_in_pi)





