import math

class Vector:
    """
    Represents a 2D vector with basic vector operations.
    
    Attributes:
        x (float): X coordinate of the vector.
        y (float): Y coordinate of the vector.
    """

    def __init__(self, x: float = 0, y: float = 0) -> None:
        """
        Initializes a new Vector instance.
        
        Args:
            x (float): The X coordinate (default is 0).
            y (float): The Y coordinate (default is 0).
        """
        self._x, self._y = x, y
    
    # X coordinate
    @property
    def x(self) -> float:
        """
        Gets the X coordinate of the vector.
        
        Returns:
            float: The X coordinate.
        """
        return self._x

    @x.setter
    def x(self, new_x: float) -> None:
        """
        Sets the X coordinate of the vector.
        
        Args:
            new_x (float): The new X coordinate value.
        """
        self._x = new_x
    

    # Y coordinate
    @property
    def y(self) -> float:
        """
        Gets the Y coordinate of the vector.
        
        Returns:
            float: The Y coordinate.
        """
        return self._y
    
    @y.setter
    def y(self, new_y: float) -> None:
        """
        Sets the Y coordinate of the vector.
        
        Args:
            new_y (float): The new Y coordinate value.
        """
        self._y = new_y
    
    # Magnitude squared
    @property
    def magnitude_squared(self) -> float:
        """
        Calculates the squared magnitude of the vector.
        
        Returns:
            float: The squared magnitude of the vector.
        """
        return self._x**2 + self._y**2
    
    @property
    def magnitude(self) -> float:
        """
        Calculates the magnitude of the vector.
        
        Returns:
            float: The magnitude of the vector.
        """
        return math.sqrt(self.magnitude_squared)
    
    @property
    def as_list(self) -> list:
        """
        Converts the vector coordinates to a list.
        
        Returns:
            list: A list containing the X and Y coordinates of the vector.
        """
        return [self.x, self.y]

    # Error/exception invoking
    def __raise_instance_error(self, instance: str) -> None:
        """
        Raises a ValueError if an incorrect instance type is passed.
        
        Args:
            instance (str): The expected instance type name.
        
        Raises:
            ValueError: If the argument is not the expected instance type.
        """
        raise ValueError(f"Passed parameter is not a '{instance}' instance.")

    # Operations (overriding)
    def __add__(self, other):
        """
        Adds two vectors.
        
        Args:
            other (Vector): The vector to add.
        
        Returns:
            Vector: A new vector that is the sum of this vector and 'other'.
        
        Raises:
            ValueError: If 'other' is not a Vector instance.
        """
        if (not isinstance(other, Vector)):
            self.__raise_instance_error("Vector")

        return Vector(self._x + other.x, self._y + other.y)

    def __sub__(self, other):
        """
        Subtracts another vector from this vector.
        
        Args:
            other (Vector): The vector to subtract.
        
        Returns:
            Vector: A new vector that is the result of subtracting 'other' from this vector.
        
        Raises:
            ValueError: If 'other' is not a Vector instance.
        """
        if (not isinstance(other, Vector)):
            self.__raise_instance_error("Vector")
        
        return Vector(self._x - other.x, self._y - other.y)
    
    def __rmul__(self, number: float):
        """
        Multiplies the vector by a scalar from the right.
        
        Args:
            number (float): The scalar value to multiply.
        
        Returns:
            Vector: A new vector that is the result of scalar multiplication.
        """
        return Vector(number * self._x, number * self._y)
    
    def __mul__(self, number: float):
        """
        Multiplies the vector by a scalar from the left.
        
        Args:
            number (float): The scalar value to multiply.
        
        Returns:
            Vector: A new vector that is the result of scalar multiplication.
        """
        return self.__rmul__(number)

    def __truediv__(self, number: float):
        """
        Divides the vector by a scalar.
        
        Args:
            number (float): The scalar value to divide by.
        
        Returns:
            Vector: A new vector that is the result of scalar division.
        """
        return 1 / number * self

    def __str__(self) -> str:
        """
        Returns the string representation of the vector.
        
        Returns:
            str: The string representation of the vector.
        """
        return __repr__()
    
    def __repr__(self) -> str:
        """
        Returns the official string representation of the vector.
        
        Returns:
            str: The official string representation of the vector.
        """
        return f"({self._x}, {self._y})"
