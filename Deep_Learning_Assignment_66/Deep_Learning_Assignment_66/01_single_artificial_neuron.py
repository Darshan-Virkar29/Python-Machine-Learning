import math

# Input values
x1 = 2
x2 = 3

# Weights
w1 = 0.4
w2 = 0.6

# Bias
bias = 0.5

# 1. Calculate weighted sum
weighted_sum = (x1 * w1) + (x2 * w2) + bias

# 2. Sigmoid activation function
output = 1 / (1 + math.exp(-weighted_sum))

# Display results
print("Single Artificial Neuron")
print("-" * 30)
print(f"Weighted Sum = {weighted_sum:.2f}")
print(f"Sigmoid Output = {output:.4f}")

# 3. Final output
print(f"Final Output = {output:.4f}")

# 4. Explanation
if output >= 0.5:
    print("Explanation: The output is closer to 1, so the neuron is activated.")
else:
    print("Explanation: The output is closer to 0, so the neuron is not activated.")
