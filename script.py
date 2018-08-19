from neuralnetwork import NeuralNetwork
import matplotlib.pyplot as plt
import numpy as np
import random
import math
networks = []
for i in range(10):
    networks.append(NeuralNetwork([2, 2, 2, 1], -1, 1, -1, 1))

yeet = None

losse = []


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


dataSet = []
answersSet = []
for i in range(10):
    val1 = random.randint(-1000, 1000)
    val2 = random.randint(-1000, 1000)
    dataSet.append([val1/1000, val2/1000])
    answersSet.append([val1/1000 + val2/1000])
for runs in range(10000):

    losses = []
    for network in networks:
        losses.append({"loss": network.runMultipleAndCalculateLoss(
            dataSet, answersSet, 1), "network": network})

    # new generation
    bestNets = []
    for loss in losses:
        if len(bestNets) < 3:
            bestNets.append(loss)
        else:
            smallestIndex = -1
            biggestLoss = 0

            for index in range(len(bestNets)):
                best = bestNets[index]
                if loss["loss"] < best["loss"] and best["loss"] > biggestLoss:
                    smallestIndex = index
                    biggestLoss = best["loss"]
            if smallestIndex != -1:
                bestNets[smallestIndex] = loss

    if runs % 32 == 0:
        for best in bestNets:
            print(best["loss"])
        print(runs, "\n")

    losse.append(bestNets[0]["loss"])

    yeet = bestNets[0]["network"]

    if bestNets[0]["loss"] < 0.001:
        break
    networks = []
    for best in bestNets:
        networks.append(best["network"])
    while len(networks) < 10:
        net = random.randint(0, 2)
        networks.append(bestNets[net]
                        ["network"].duplicate().mutate(0.5, 0.2))


print([-65, 455], [-65 + 455], network.run([-65/1000, 455/1000])[0]*1000)
yeet.printData()
plt.plot(losse)
plt.show()
# console.log(network.run([0.1, 0.4]));
# console.log(network.run([0.4, 0.6]));
