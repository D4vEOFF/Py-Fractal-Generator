
from abc import ABC

class IFractalIterable(ABC):
    """
    An abstract base class representing the iterable behavior of a fractal.
    """

    @property
    def total_iterations(self):
        """
        Returns the total number of iterations performed.
        
        Returns:
            int: Total number of iterations.
        """
        pass
    
    def iterate(self, iterations: int) -> None:
        """
        Performs a specified number of iterations.
        
        Parameters:
            iterations (int): The number of iterations to perform.
        """
        pass
