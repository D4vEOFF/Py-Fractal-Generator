from abc import ABC

from ..vector import Vector

class IFractalTransformable(ABC):
    """
    An abstract base class representing the transformable behavior of a fractal.
    """
    
    def scale(self, factor: float) -> None:
        """
        Scales the fractal by a given factor.
        
        Parameters:
            factor (float): The factor by which to scale the fractal.
        """
        pass

    def translate(self, translation_vector: Vector) -> None:
        """
        Translates the fractal by a given vector.
        
        Parameters:
            translation_vector (Vector): The vector by which to translate the fractal.
        """
        pass

    def rotate(self, angle: float) -> None:
        """
        Rotates the fractal by a given angle.
        
        Parameters:
            angle (float): The angle in degrees by which to rotate the fractal.
        """
        pass
