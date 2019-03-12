from neuralnetwork import NeuralNetwork
import matplotlib.pyplot as plt
import numpy as np
import random
import math

network = NeuralNetwork([2, 2, 1], -1, 1, -1, 1)
losse = []

dataSet = [[1, 0], [0, 0], [0, 1], [1, 1]]
answersSet = [[1], [0], [0], [1]]
# for i in range(50):
#     val1 = random.randint(-1000, 1000)
#     val2 = random.randint(-1000, 1000)
#     dataSet.append([val1/1000.0, val2/1000.0])
#     answersSet.append([val1/1000.0 + val2/1000.0])

for runs in range(10000):

    myLoss = network.runMultipleAndCalculateLoss(dataSet, answersSet)
    if runs % 50 == 0:
        print(myLoss, runs)

    losse.append(myLoss)

    # if myLoss < 0.0001:
    #    break

    network.backpropagate(dataSet, answersSet, 0.03, myLoss)

network.printData()
plt.plot(losse)
plt.show()
while True:
    one = int(input('1: '))
    two = int(input('2: '))
    print(network.run([one, two])[0])

# console.log(network.run([0.1, 0.4]));
# console.log(network.run([0.4, 0.6]));
