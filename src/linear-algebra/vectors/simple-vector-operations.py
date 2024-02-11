import numpy as np

# Simple vector arithmetic

v = np.array([1, -3, 2])
w = np.array([4, 2, 1])

# Vector addition
sum_vw = v + w
print("vector sum: ", sum_vw)

# Scalar multiplication
v_scaled = 2*v
print("v scaled: ", v_scaled)

# Negative vector
w_negative = -(w)
print("negative vector w: ", w_negative)

# Subtract w from v
diff_1 = v + w_negative
diff_2 = v - w

print("diff1: ", diff_1)
print("diff2: ", diff_2)


