from activations.Sigmoid import Sigmoid
from activations.HyperbolicTangent import HyperbolicTangent
from nn import NeuralNetwork
from neuron import Neuron
from layer import Layer
import matplotlib.pyplot as plt
import numpy as np


nn = NeuralNetwork()
input_layer = Layer()
input_layer.add_neurons(4)
hidden_layer = Layer()
hidden_layer.add_neurons(8)
output_layer = Layer()
output_layer.add_neurons(2)
nn.add_layer(input_layer)
nn.add_layer(hidden_layer)
nn.add_layer(output_layer)
nn.init_weights()






neuron = Neuron()
neuron.set_activation(HyperbolicTangent())


# X értékek létrehozása -5 és 5 között
x_values = np.linspace(-5, 5, 400)

# Aktivációs értékek és derivált értékek számítása
y_values = [neuron.activation.activate(x) for x in x_values]
dy_values = [neuron.activation.derivate(x) for x in x_values]

# Grafikon megjelenítése
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label=f'{neuron.activation.title} Activation', color='b')
plt.plot(x_values, dy_values, label=f'{neuron.activation.title} Derivative', color='r', linestyle='--')
plt.title(f'{neuron.activation.title} Activation and Derivative')
plt.xlabel('Input')
plt.ylabel('Output')
plt.legend()
plt.grid(True)
plt.show()