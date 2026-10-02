# 10.a) write the program to demonstrate simple neural network

import numpy as np
from sklearn.neural_network import MLPClassifier

# Input data:
# [Study Hours, Attendance %]
X = np.array([
    [1, 50],
    [2, 55],
    [2, 60],
    [3, 65],
    [4, 70],
    [5, 75],
    [6, 80],
    [7, 85],
    [8, 90],
    [9, 95]
])

# Output:
# 0 = Fail, 1 = Pass
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# Create Neural Network
model = MLPClassifier(
    hidden_layer_sizes=(5,),
    activation='relu',
    solver='lbfgs',
    max_iter=2000,
    random_state=1
)

# Train the model
model.fit(X, y)

# Test data
test_data = np.array([
    [2, 55],
    [5, 75],
    [8, 90]
])

# Make predictions
predictions = model.predict(test_data)

# Display results
for i in range(len(test_data)):
    if predictions[i] == 1:
        result = "Pass"
    else:
        result = "Fail"

    print("Study Hours:", test_data[i][0],
          "Attendance:", test_data[i][1], "%",
          "Prediction:", result)