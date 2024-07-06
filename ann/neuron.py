"""
Neuron Class with Configurable Activation Function, Weights, and Bias
"""

from activations.ActivationModule import ActivationModule
from activations.Sigmoid import Sigmoid
from typing import List

class Neuron:
    """
    A class used to represent a neuron with configurable activation function,
    weights, and bias.
    
    Attributes
    ----------
    activation : ActivationModule
        The activation function of the neuron.
    weights : List[float]
        The weights associated with the neuron's inputs.
    bias : float
        The bias term of the neuron.
    
    Methods
    -------
    set_activation(activation: ActivationModule) -> None
        Sets the activation function of the neuron.
    get_activation() -> ActivationModule
        Returns the current activation function of the neuron.
    set_weights(weights: List[float]) -> None
        Sets the weights of the neuron.
    get_weights() -> List[float]
        Returns the current weights of the neuron.
    set_bias(bias: float) -> None
        Sets the bias of the neuron.
    get_bias() -> float
        Returns the current bias of the neuron.
    """
    
    def __init__(self) -> None:
        """
        Initializes the Neuron class with a specified number of inputs.
        
        Parameters
        ----------
        num_inputs : int
            The number of inputs to the neuron.
        
        Attributes
        ----------
        activation : ActivationModule
            The activation function of the neuron, initially set to None.
        weights : List[float]
            The weights associated with the neuron's inputs, initialized to zero.
        bias : float
            The bias term of the neuron, initialized to zero.
        """
        self.activation: ActivationModule = None
        self.weights: List[float] = []
        self.bias: float = 0.0

    def set_activation(self, activation: ActivationModule) -> None:
        """
        Sets the activation function of the neuron.
        
        Parameters
        ----------
        activation : ActivationModule
            The activation function to be set.
        """
        self.activation = activation

    def get_activation(self) -> ActivationModule:
        """
        Returns the current activation function of the neuron.
        
        Returns
        -------
        ActivationModule
            The current activation function of the neuron.
        """
        return self.activation

    def set_weights(self, weights: List[float]) -> None:
        """
        Sets the weights of the neuron.
        
        Parameters
        ----------
        weights : List[float]
            The weights to be set.
        """
        self.weights = weights

    def get_weights(self) -> List[float]:
        """
        Returns the current weights of the neuron.
        
        Returns
        -------
        List[float]
            The current weights of the neuron.
        """
        return self.weights

    def set_bias(self, bias: float) -> None:
        """
        Sets the bias of the neuron.
        
        Parameters
        ----------
        bias : float
            The bias to be set.
        """
        self.bias = bias

    def get_bias(self) -> float:
        """
        Returns the current bias of the neuron.
        
        Returns
        -------
        float
            The current bias of the neuron.
        """
        return self.bias
