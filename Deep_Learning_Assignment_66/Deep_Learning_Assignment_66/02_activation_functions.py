import numpy as np
import matplotlib.pyplot as plt

# Input values from -10 to 10
x = np.linspace(-10, 10, 400)

# Activation functions
sigmoid = 1 / (1 + np.exp(-x))
relu = np.maximum(0, x)
tanh = np.tanh(x)

# Plot Sigmoid
plt.figure(figsize=(8, 5))
plt.plot(x, sigmoid)
plt.title("Sigmoid Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid(True)
plt.show()

# Plot ReLU
plt.figure(figsize=(8, 5))
plt.plot(x, relu)
plt.title("ReLU Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid(True)
plt.show()

# Plot Tanh
plt.figure(figsize=(8, 5))
plt.plot(x, tanh)
plt.title("Tanh Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid(True)
plt.show()

print("Activation Functions")
print("-" * 30)
print("1. Sigmoid: Produces values between 0 and 1. Commonly used for binary classification output.")
print("2. ReLU: Returns 0 for negative values and x for positive values. Commonly used in hidden layers.")
print("3. Tanh: Produces values between -1 and 1. Useful when centered output is preferred.")
