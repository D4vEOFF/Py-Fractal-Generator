
from abc import ABC

class IFractalIterable(ABC):

    @property
    def total_iterations(self):
        return self._total_iterations
    

    def iterate(self, iterations: int) -> None:
        pass