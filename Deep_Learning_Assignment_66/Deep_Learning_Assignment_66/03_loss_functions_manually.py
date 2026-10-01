import math

# Actual and predicted values
actual_values = [1, 0, 1, 1]
predicted_values = [0.9, 0.2, 0.8, 0.7]

# 1. Mean Squared Error (MSE)
mse = sum((actual - predicted) ** 2
          for actual, predicted in zip(actual_values, predicted_values)) / len(actual_values)

# 2. Binary Cross Entropy (BCE)
bce = -sum(
    actual * math.log(predicted) +
    (1 - actual) * math.log(1 - predicted)
    for actual, predicted in zip(actual_values, predicted_values)
) / len(actual_values)

# Display values
print("Loss Functions")
print("-" * 30)
print("Actual values:   ", actual_values)
print("Predicted values:", predicted_values)
print(f"MSE = {mse:.4f}")
print(f"Binary Cross Entropy = {bce:.4f}")

# Explanation
print("\nUse of loss functions:")
print("MSE is commonly used for regression problems because it measures squared differences.")
print("Binary Cross Entropy is commonly used for binary classification because it measures")
print("the difference between actual binary labels and predicted probabilities.")
