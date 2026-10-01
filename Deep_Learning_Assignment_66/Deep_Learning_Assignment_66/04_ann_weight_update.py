# Demonstration of weight update using gradient descent

# Input, initial weight, target output and learning rate
x = 2.0
weight = 0.4
target = 1.0
learning_rate = 0.1
bias = 0.0

# 1. Calculate prediction
prediction = (x * weight) + bias

# 2. Calculate error
error = target - prediction

# 3. Calculate gradient
# For a simple linear neuron with squared-error style update:
# gradient = error * input
gradient = error * x

# 4. Update weight using gradient descent
new_weight = weight + (learning_rate * gradient)

# Display results
print("ANN Weight Update Using Gradient Descent")
print("-" * 45)
print(f"Input (x)          = {x}")
print(f"Old Weight         = {weight}")
print(f"Target Output      = {target}")
print(f"Learning Rate      = {learning_rate}")
print(f"Prediction         = {prediction:.4f}")
print(f"Error              = {error:.4f}")
print(f"Gradient           = {gradient:.4f}")
print(f"Updated Weight     = {new_weight:.4f}")
