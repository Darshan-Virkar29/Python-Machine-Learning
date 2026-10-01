# Deep Learning Assignment 68
# 1. Manually perform convolution

image = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

kernel = [
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
]

rows = len(image)
cols = len(image[0])
k_size = len(kernel)

feature_map = []

for i in range(rows - k_size + 1):
    row = []
    for j in range(cols - k_size + 1):
        total = 0

        for ki in range(k_size):
            for kj in range(k_size):
                total += image[i + ki][j + kj] * kernel[ki][kj]

        row.append(total)

    feature_map.append(row)

print("Input Image:")
for row in image:
    print(row)

print("\nKernel:")
for row in kernel:
    print(row)

print("\nFeature Map:")
for row in feature_map:
    print(row)
