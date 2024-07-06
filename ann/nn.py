from typing import List
from layer import Layer

class NeuralNetwork:
    def __init__(self) -> None:
        self.layers: List[Layer] = None

    def add_layer(self, layer: Layer) -> None:
        self.layers.append(layer)

    def init_weights(self) -> None:
        for i in range(self.layers.count):
            pass