import numpy as np

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

def proja_U(u: np.ndarray, a: np.ndarray) -> np.ndarray:

    if not isinstance(u, np.ndarray) or not isinstance(a, np.ndarray):
        raise TypeError('Expected arr to be an np.ndarray')

    dot_ua = u.dot(a)
    norm_a = np.linalg.norm(a)

    return (dot_ua/norm_a ** 2) * a


u = get_vector_input("Enter the first vector in the format (a1, a2, a3): ")
v = get_vector_input("Enter the second vector in the format (a1, a2, a3): ")

print("Vector u:",u)
print("Vector v:", v)
print("projection: ", proja_U(np.array(u), np.array(v)))


