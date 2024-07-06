from activations.Sigmoid import Sigmoid
from activations.HyperbolicTangent import HyperbolicTangent
from neuron import Neuron
import matplotlib.pyplot as plt
import numpy as np


neuron = Neuron(0)
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