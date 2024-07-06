"""
Abstract Base Class for Activation Functions
"""

from abc import ABC, abstractmethod

class ActivationModule(ABC):
    """
    An abstract base class used to represent an activation function.
    
    Attributes
    ----------
    title : str
        The name of the activation function.
    
    Methods
    -------
    activate(sum: float) -> float
        Abstract method to compute the activation function.
    
    derivate(sum: float) -> float
        Abstract method to compute the derivative of the activation function.
    """

    title: str

    @abstractmethod
    def activate(self, sum: float) -> float:
        """
        Compute the activation function.
        
        Parameters
        ----------
        sum : float
            The input value.
        
        Returns
        -------
        float
            The result of the activation function.
        """
        pass

    @abstractmethod    
    def derivate(self, sum: float) -> float:
        """
        Compute the derivative of the activation function.
        
        Parameters
        ----------
        sum : float
            The input value.
        
        Returns
        -------
        float
            The derivative of the activation function.
        """
        pass
