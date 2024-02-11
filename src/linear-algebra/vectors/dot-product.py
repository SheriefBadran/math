import numpy as np
import math

# Consider the vectors u = (2, -1, 1) and v = (1, 1, 2). Find u • v and determine the angel betwen u and v

def calculate_vectors_angle(u: np.ndarray, v: np.ndarray, in_radians: bool = True) -> float :

    if not isinstance(u, np.ndarray) or not isinstance(v, np.ndarray):
        raise TypeError('Expected array to be an np.ndarray')
    
    if not isinstance(in_radians, bool):
        raise TypeError('Expected in_radians to be a boolean')
    
    dot_uv = u.dot(v)
    norm_u = np.linalg.norm(u)
    norm_v = np.linalg.norm(v)
    
    cos_theta = dot_uv/(norm_u * norm_v)
    theta = np.arccos(cos_theta)
    return theta if in_radians else math.degrees(theta)

rad_angle_uv = calculate_vectors_angle(np.array([2, -1, 1]), np.array([1, 1, 2]), in_radians=True)

print("Angle between u and v: ", rad_angle_uv)





