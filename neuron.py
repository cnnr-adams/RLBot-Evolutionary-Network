import math


class Neuron:

    def __init__(self, id, bias, connections):
        self.input = 0
        self.id = id
        self.bias = bias
        self.connections = connections

    def setInput(self, input):
        self.input += input

    def getOutput(self):
        temp = self.input - self.bias
        self.input = 0
        return temp

    def forwardOutput(self, output):
        for connection in self.connections:
            connection.feedThrough(sigmoid(output))


def sigmoid(x):
    return 1 / (1 + math.exp(-x))
