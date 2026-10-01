import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Features:
# [Income, Credit Score, Loan Amount, Existing EMI, Employment Status]
#
# Employment Status:
# 0 = Not Stable
# 1 = Stable
#
# Output:
# 0 = Loan rejected
# 1 = Loan approved

X = np.array([
    [25000, 600, 200000, 10000, 0],
    [40000, 700, 300000, 8000, 1],
    [60000, 750, 500000, 12000, 1],
    [20000, 550, 150000, 15000, 0],
    [80000, 800, 700000, 10000, 1],
    [35000, 650, 250000, 9000, 1],
    [18000, 500, 100000, 12000, 0],
    [90000, 850, 800000, 15000, 1],
    [30000, 580, 200000, 14000, 0],
    [70000, 780, 600000, 10000, 1]
])

y = np.array([0, 1, 1, 0, 1, 1, 0, 1, 0, 1])

# 1. Preprocess categorical values
# Employment Status is already encoded:
# 0 = Not Stable, 1 = Stable

# 2. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. Apply scaling
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

# 5. Evaluate model
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

print("Loan Approval Prediction")
print("-" * 35)
print(f"Test Accuracy: {accuracy * 100:.2f}%")

# Test input from the assignment
new_applicant = np.array([[55000, 720, 400000, 10000, 1]])
new_applicant_scaled = scaler.transform(new_applicant)
prediction = model.predict(new_applicant_scaled)[0]

print("Test Input:", new_applicant.tolist())

if prediction == 1:
    print("Prediction: Loan Approved")
else:
    print("Prediction: Loan Rejected")
