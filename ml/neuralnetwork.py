from neuron import Neuron
from connection import Connection
from neuraldiagram import NeuralDiagram
import copy
import random


class NeuralNetwork:
    def __init__(self, neuronCount, minBias, maxBias, minWeight, maxWeight):
        self.neurons = [[]]
        for j in range(len(neuronCount)-1, -1, -1):
            amount = neuronCount[j]
            for i in range(amount):
                # First go, output neurons
                if j == len(neuronCount) - 1:
                    self.neurons[0].append(
                        Neuron(f"{j},{i}", random.uniform(minBias, maxBias), []))
                else:
                    nextLayer = []
                    if j != len(neuronCount) - 1:
                        for neuron in self.neurons[len(neuronCount) - 2 - j]:
                            nextLayer.append(Connection(
                                neuron, random.uniform(minWeight, maxWeight)))
                    if len(self.neurons) > len(neuronCount) - 1 - j:
                        if j == 0:
                            self.neurons[len(neuronCount) - 1 -
                                         j].append(Neuron(f"{j},{i}", 0, nextLayer))
                        else:
                            self.neurons[len(neuronCount) - 1 - j].append(
                                Neuron(f"{j},{i}", random.uniform(minBias, maxBias), nextLayer))
                    else:
                        if j == 0:
                            self.neurons.append(
                                [Neuron(f"{j},{i}", 0, nextLayer)])
                        else:
                            self.neurons.append(
                                [Neuron(f"{j},{i}", random.uniform(minBias, maxBias), nextLayer)])

        self.neurons = self.neurons[::-1]
        # self.printData()

    def printData(self):
        print(NeuralDiagram(self).createDiagram())

    def run(self, inputs):
        outputs = []
        for index in range(len(self.neurons)):
            for nIndex in range(len(self.neurons[index])):
                neuron = self.neurons[index][nIndex]
                if index == 0:
                    neuron.setInput(inputs[nIndex])
                    neuron.forwardOutput(neuron.getOutput())
                elif index == len(self.neurons) - 1:
                    outputs.append(neuron.getOutput())
                else:
                    neuron.forwardOutput(neuron.getOutput())
        return outputs

    def backpropagate(self, inputs, correctOutput, C, lastLoss):
       # print(lastLoss)
        W = 0.01
        for index in range(len(self.neurons)):
            for idx in range(len(self.neurons[index])):
                neuron = self.neurons[index][idx]
                if index != 0:
                    neuron.bias += W
                    der = (self.runMultipleAndCalculateLoss(
                        inputs, correctOutput) - lastLoss) / W
                    neuron.bias -= W
                    neuron.bias = neuron.bias - der * C
                for connection in neuron.connections:
                    connection.weight += W
                    der = (self.runMultipleAndCalculateLoss(
                        inputs, correctOutput) - lastLoss) / W
                    connection.weight -= W
                    connection.weight = connection.weight - der * C
        return self

    def mutate(self, mutateRate, mutateAmount):
        for neuron0, index in self.neurons:
            for neuron in self.neurons[index]:
                print(neuron)
              # neuron = self.neurons[index][idx]
                if index != 0:
                    if random.uniform(0, 1) < mutateRate:
                        neuron.bias += random.uniform(-mutateAmount,
                                                      mutateAmount)
                for connection in neuron.connections:
                    if (random.uniform(0, 1) < mutateRate):
                        connection.weight += random.uniform(-mutateAmount,
                                                            mutateAmount)
        return self

    def runMultipleAndCalculateLoss(self, inputs, correctOutput):
       # print("new")
        loss = 0
        for index in range(len(inputs)):
            output = self.run(inputs[index])
            for idx in range(len(correctOutput[index])):
              #  print(inputs[index], correctOutput[index][idx], output[idx], C *
                   #   (correctOutput[index][idx] - output[idx]) ** 2)
                loss += (correctOutput[index][idx] - output[idx]) ** 2
            loss /= len(correctOutput[index])
        loss /= len(inputs)
        return loss

    def duplicate(self):
        return copy.deepcopy(self)
