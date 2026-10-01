import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Features:
# [Age, Monthly Charges, Tenure, Number of Complaints, Customer Support Calls]

X = np.array([
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
])

# 0 = Customer will stay
# 1 = Customer will leave
y = np.array([0, 0, 1, 1, 0, 0, 1, 1, 0, 1])

# 1. Load/create dataset and clean it
# Check for missing values and duplicate rows.
print("Missing values:", np.isnan(X).sum())
print("Duplicate rows:", len(X) - len(np.unique(X, axis=0)))

# 2. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. Apply StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Train FNN model
model = MLPClassifier(
    hidden_layer_sizes=(8,),
    activation="relu",
    solver="lbfgs",
    max_iter=5000,
    random_state=42
)
model.fit(X_train_scaled, y_train)

# 5. Evaluate accuracy
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

print("\nCustomer Churn Prediction")
print("-" * 35)
print(f"Test Accuracy: {accuracy * 100:.2f}%")

# Test input from the assignment
new_customer = np.array([[46, 1450, 5, 6, 9]])
new_customer_scaled = scaler.transform(new_customer)
prediction = model.predict(new_customer_scaled)[0]

print("Test Input:", new_customer.tolist())

if prediction == 1:
    print("Prediction: Customer may leave")
else:
    print("Prediction: Customer will stay")
