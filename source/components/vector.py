
import math

class Vector:
    """Represents a 2D vector."""

    def __init__(self, x: float = 0, y: float = 0) -> None:
        self._x, self._y = x, y
    
    # X coordinate
    @property
    def x(self) -> float:
        """X coordinate."""
        return self._x

    @x.setter
    def x(self, new_x: float) -> None:
        self._x = new_x
    

    # Y coordinate
    @property
    def y(self) -> float:
        """Y coordinate."""
        return self._y
    
    @y.setter
    def y(self, new_y: float) -> None:
        self._y = new_y
    
    # Magnitude squared
    @property
    def magnitude_squared(self) -> float:
        """Vector magnitude squared."""
        return self._x**2 + self._y**2
    
    @property
    def magnitude(self) -> float:
        """Vector magnitude."""
        return math.sqrt(self.magnitude_squared)

    # Error/exception invoking
    def __raise_instance_error(self, instance: str) -> None:
        raise ValueError(f"Passed parameter is not a '{instance}' instance.")

    # Operations (overriding)
    def __add__(self, other):
        if (not isinstance(other, Vector)):
            self.__raise_instance_error("Vector")

        return Vector(self._x + other.x, self._y + other.y)

    def __sub__(self, other):
        if (not isinstance(other, Vector)):
            self.__raise_instance_error("Vector")
        
        return Vector(self._x - other.x, self._y - other.y)
    
    def __rmul__(self, number: float):
        return Vector(number * self._x, number * self._y)
    
    def __mul__(self, number: float):
        return self.__rmul__(number)

    def __truediv__(self, number: float):
        return 1 / number * self

    def __str__(self) -> str:
        return f"({self._x}, {self._y})"