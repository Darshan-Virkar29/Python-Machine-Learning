# Deep Learning Assignment 68
# 3. Demonstrate Flattening

matrix = [
    [6, 4],
    [8, 6]
]

# Convert the 2D matrix into a 1D vector
flatten_output = []

for row in matrix:
    for value in row:
        flatten_output.append(value)

print("Input Matrix:")
for row in matrix:
    print(row)

print("\nFlatten Output:")
print(flatten_output)

print("\nRole of Flatten Layer in CNN:")
print("The flatten layer converts a multi-dimensional feature map into a")
print("one-dimensional vector so it can be passed to fully connected layers")
print("for final classification or prediction.")
