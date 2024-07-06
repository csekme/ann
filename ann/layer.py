"""
Layer Class for Neural Networks
"""

from typing import List
from activations.ActivationModule import ActivationModule
from neuron import Neuron

class Layer:
    """
    A class used to represent a layer in a neural network.
    
    Attributes
    ----------
    neurons : List[Neuron]
        The list of neurons in the layer.
    
    Methods
    -------
    add_neuron(neuron: Neuron) -> None
        Adds a neuron to the layer.
    get_neurons() -> List[Neuron]
        Returns the list of neurons in the layer.
    set_activations(activation: ActivationModule) -> None
        Sets the activation function for all neurons in the layer.
    """
    
    def __init__(self) -> None:
        """
        Initializes the Layer class with a specified number of neurons and inputs per neuron.
        
        Parameters
        ----------
        num_neurons : int
            The number of neurons in the layer.
        num_inputs_per_neuron : int
            The number of inputs per neuron.
        
        Attributes
        ----------
        neurons : List[Neuron]
            The list of neurons in the layer, each initialized with the specified number of inputs.
        """
        self.neurons: List[Neuron] = []

    def add_neurons(self, number_of_neurons: int) -> None:
        """
        Adds a specified number of neurons to the layer.
        
        Parameters
        ----------
        number_of_neurons : int
            The number of neurons to be added.
        """
        for _ in range(number_of_neurons):
            self.add_neuron(Neuron())


    def add_neuron(self, neuron: Neuron) -> None:
        """
        Adds a neuron to the layer.
        
        Parameters
        ----------
        neuron : Neuron
            The neuron to be added.
        """
        self.neurons.append(neuron)

    def get_neurons(self) -> List[Neuron]:
        """
        Returns the list of neurons in the layer.
        
        Returns
        -------
        List[Neuron]
            The list of neurons in the layer.
        """
        return self.neurons

    def set_activations(self, activation: ActivationModule) -> None:
        """
        Sets the activation function for all neurons in the layer.
        
        Parameters
        ----------
        activation : ActivationModule
            The activation function to be set for all neurons.
        """
        for neuron in self.neurons:
            neuron.set_activation(activation)
