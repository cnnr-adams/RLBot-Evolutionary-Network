class NeuralDiagram:
    def __init__(self, network):
        self.network = network

    def createDiagram(self):
        data = ""
        for x in range(len(self.network.neurons)):
            s = f"LAYER {x}: \n"
            data += s
            for y in range(len(self.network.neurons[x])):
                neuron = self.network.neurons[x][y]
                if neuron:
                    data += f"< ID: ({neuron.id}), B: {neuron.bias}, C: " + "{"
                    for connection in neuron.connections:
                        data += f"[W:{connection.weight} -> ID: ({connection.output.id})]"

                data += "} >\n"
            data += "\n"
        return data
