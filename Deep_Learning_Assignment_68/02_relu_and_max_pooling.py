# Deep Learning Assignment 68
# 2. Demonstrate ReLU and 2x2 Max Pooling

feature_map = [
    [3, 3, 3],
    [0, 0, 0],
    [-3, -3, -3]
]

# ReLU: negative values become 0; non-negative values remain unchanged
relu_output = []

for row in feature_map:
    relu_row = []
    for value in row:
        relu_row.append(max(0, value))
    relu_output.append(relu_row)

# 2x2 Max Pooling with stride 2
pool_size = 2
stride = 2

pooled_output = []

for i in range(0, len(relu_output) - pool_size + 1, stride):
    row = []
    for j in range(0, len(relu_output[0]) - pool_size + 1, stride):
        values = []

        for pi in range(pool_size):
            for pj in range(pool_size):
                values.append(relu_output[i + pi][j + pj])

        row.append(max(values))

    pooled_output.append(row)

print("Input Feature Map:")
for row in feature_map:
    print(row)

print("\nReLU Output:")
for row in relu_output:
    print(row)

print("\n2x2 Max Pooling Output:")
for row in pooled_output:
    print(row)

print("\nWhy does pooling reduce size?")
print("Pooling summarizes a local region using a value such as its maximum.")
print("Therefore, fewer values are retained, which reduces the spatial dimensions")
print("and computational cost while preserving important features.")
