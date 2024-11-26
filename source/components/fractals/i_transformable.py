
from abc import ABC

from ..vector import Vector

class IFractalTransformable(ABC):
    
    def scale(self, factor: float) -> None:
        pass

    def translate(self, translation_vector: Vector) -> None:
        pass

    def rotate(self, angle: float) -> None:
        pass