

inputs = [1, 2, 3, 2.5]
weights1 = [0.2, 0.8, -0.5, 1.0]
weights2 = [0.5, -0.91, -0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]

bias1 = 2
bias2 = 3
bias3 = 0.5

biases=[bias1,bias2,bias3]


weights = []
weights.append(weights1)
weights.append(weights2)
weights.append(weights3)

outputs=[]
for j in range(0,3):
    nweights = weights[j]
    output=0
    for i in range(0,4):
        output = output + nweights[i] * inputs[i]
    output = output + biases[j]
    outputs.append(output)

print(outputs)
