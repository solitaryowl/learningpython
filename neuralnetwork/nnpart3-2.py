import numpy as np

inputs = [1, 2, 3, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2.0

output = np.dot(weights, inputs) + bias
print(output)


inputs = [1, 2, 3, 5]
weights = [[2, 2, 2, 2], [5, 5, 5, 5], [7, 7, 7, 7]]
biases = [0.4, 0.6, 2]

output = np.dot(weights, inputs) + biases
print(output)
