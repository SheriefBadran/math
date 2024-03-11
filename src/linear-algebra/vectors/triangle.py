import numpy as np
from numpy.linalg import norm

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
            print("Error: Please enter a valid vector in the format (a1, a2, a3) with integer values.")

def calculate_triangle_area(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> float :

    if not isinstance(a, np.ndarray) or not isinstance(b, np.ndarray) or not isinstance(c, np.ndarray):
        raise TypeError('Point has to be an np.ndarray')
    
    return 1/2 * norm(np.cross(b - a, c - a))

a = get_vector_input("Enter the first point in the format (x, y, z): ")
b = get_vector_input("Enter the second point in the format (x, y, z): ")
c = get_vector_input("Enter the third point in the format (x, y, z): ")

area = calculate_triangle_area(np.array(a), np.array(b), np.array(c))
print("Triangle area: ", area)