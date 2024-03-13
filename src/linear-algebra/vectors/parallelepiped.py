import numpy as np
from numpy import linalg

def get_vector_input(promt):
    while True:
        vector_input = input(promt)
        try:
            vector = [int(item) for item in vector_input.strip("()").split(',')]
            if len(vector) == 3:
                return vector
            else:
                print("Error: The vector can only contain three components.")
        except ValueError:
            print("Error: Please enter a valid vector in the format (x, y, z) with integer values.")

def calculate_parallelepiped_volume(u: np.ndarray, v: np.ndarray, w: np.ndarray) -> float :

    if not isinstance(u, np.ndarray) or not isinstance(v, np.ndarray) or not isinstance(w, np.ndarray):
        raise TypeError('Vector has to be an np.ndarray')
    
    A = np.array([u, v, w])
    return linalg.det(A)

u = get_vector_input("Enter vector u in the format (u1, u2, u3): ")
v = get_vector_input("Enter vector v in the format (v1, v2, v3): ")
w = get_vector_input("Enter vector w in the format (w1, w2, w3): ")

# Find the volume of the parallelepiped with sides u, v and w
# V = 16 for u = (2, -6, 2), v = (0, 4, -2), w = (2, 2, -4) and V = 45 for u = (3, 1, 2), v = (4, 5, 1), w = (1, 2, 4)
volume = calculate_parallelepiped_volume(np.array(u), np.array(v), np.array(w))
print("Parallelepiped volume: ", volume)