"""
Sigmoid Activation Function and its Derivative
"""

from activations.ActivationModule import ActivationModule
import math

class Sigmoid(ActivationModule):
    """
    A class used to represent the Sigmoid Activation Function
    
    Attributes
    ----------
    title : str
        The name of the activation function.
    
    Methods
    -------
    activate(sum: float) -> float
        Computes the sigmoid of the input.
    
    derivate(sum: float) -> float
        Computes the derivative of the sigmoid function.
    """

    def __init__(self) -> None:
        """
        Initializes the Sigmoid class.
        
        Attributes
        ----------
        title : str
            The name of the activation function.
        """
        super().__init__()
        self.title = "Sigmoid"

    def activate(self, sum: float) -> float:
        """
        Compute the sigmoid of the input.
        
        Parameters
        ----------
        sum : float
            The input value.
        
        Returns
        -------
        float
            The sigmoid of the input.
        """
        return 1 / (1 + math.exp(-sum))
    
    def derivate(self, sum: float) -> float:
        """
        Compute the derivative of the sigmoid function.
        
        Parameters
        ----------
        sum : float
            The input value.
        
        Returns
        -------
        float
            The derivative of the sigmoid function.
        """
        activation = self.activate(sum)
        return activation * (1 - activation)
