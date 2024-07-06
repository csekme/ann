"""
Hyperbolic Tangent Activation Function and its Derivative
"""

from activations.ActivationModule import ActivationModule
import math

class HyperbolicTangent(ActivationModule):

    def __init__(self) -> None:
        super().__init__()
        self.title = "Hyperbolic Tangent"

    """
    A class used to represent the Hyperbolic Tangent Activation Function
    
    Methods
    -------
    activate(sum: float) -> float
        Computes the hyperbolic tangent of the input.
    
    derivate(sum: float) -> float
        Computes the derivative of the hyperbolic tangent function.
    """

    def activate(self, sum: float) -> float:
        """
        Compute the hyperbolic tangent of the input.
        
        Parameters
        ----------
        sum : float
            The input value.
        
        Returns
        -------
        float
            The hyperbolic tangent of the input.
        """
        return (2 / (1 + math.exp(-2 * sum))) - 1
    
    def derivate(self, sum: float) -> float:
        """
        Compute the derivative of the hyperbolic tangent function.
        
        Parameters
        ----------
        sum : float
            The input value.
        
        Returns
        -------
        float
            The derivative of the hyperbolic tangent function.
        """
        activation = self.activate(sum)
        return 1 - activation ** 2
