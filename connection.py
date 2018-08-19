from neuron import Neuron


class Connection:
    def __init__(self, output, weight=1):
        self.output = output
        self.weight = weight

    def feedThrough(self, input):
        self.output.setInput(input * self.weight)
