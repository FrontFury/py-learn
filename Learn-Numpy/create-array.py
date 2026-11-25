import numpy as np

# 1. Creating Arrays
arr_1d = np.array([1, 2, 3, 4, 5])                # 1D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])         # 2D array (matrix)
zeros = np.zeros((2, 3))                          # 2x3 array of zeros
sequence = np.arange(0, 10, 2)                    # [0, 2, 4, 6, 8]

# 2. Fast Math (Vectorization - no loops needed)
print(arr_1d * 2)                                 # [2, 4, 6, 8, 10]
print(arr_1d + 10)                                # [11, 12, 13, 14, 15]

# 3. Array Properties
print(arr_2d.shape)                               # (2, 3) -> 2 rows, 3 columns
print(arr_2d.dtype)                               # Data type (e.g., int64)

# 4. Indexing & Slicing
print(arr_1d[0])                                  # First element: 1
print(arr_2d[0, 1])                               # Row 0, Column 1: 2
print(arr_1d[1:4])                                # Slice: [2, 3, 4]

# 5. Built-in Statistics
print(np.mean(arr_1d))                            # Average: 3.0
print(np.max(arr_2d))                             # Max value: 6
print(np.sum(arr_2d, axis=0))                     # Sum of each column: [5, 7, 9]