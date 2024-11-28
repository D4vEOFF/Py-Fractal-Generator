from components.vector import Vector
from components.event import Event

import math

class Turtle:
    """Turtle 2D graphics."""
    def __init__(self, step: float, position: Vector = Vector(0, 0), angle: float = 0) -> None:
        """
        Initializes a new instance of the Turtle class.
        
        Parameters:
            step (float): The length of each step the turtle takes.
            position (Vector): The starting position of the turtle. Defaults to Vector(0, 0).
            angle (float): The initial direction of the turtle in degrees. Defaults to 0.
        """
        self._position = position
        self._step = step
        self._angle = (angle % 360) * math.pi / 180
        self._pen_down = False
        self._lines = []

        self._x_min, self._y_min = position.x, position.y
        self._x_max, self._y_max = position.x, position.y

        self._line_drawn = Event()

    # Events
    def add_line_drawn_subscriber(self, method):
        """
        Adds a subscriber to the event that triggers when a line is drawn.
        
        Parameters:
            method: The callback function to be called when a line is drawn.
        """
        self._line_drawn += method

    def remove_line_drawn_subscriber(self, method):
        """
        Removes a previously added subscriber from the line drawn event.
        
        Parameters:
            method: The callback function to remove.
        """
        self._line_drawn -= method

    @property
    def position(self) -> Vector:
        """
        Gets the current position of the turtle.
        
        Returns:
            Vector: A Vector object representing the current position.
        """
        return Vector(self._position.x, self._position.y)
    
    @property
    def step(self) -> float:
        """
        Gets the current step length.
        
        Returns:
            float: The step length of the turtle.
        """
        return self._step
    
    @property
    def angle(self) -> float:
        """
        Gets the current direction of the turtle in degrees.
        
        Returns:
            float: The current direction of the turtle in degrees.
        """
        return self._angle * 180 / math.pi
    
    @property
    def pen_down(self) -> bool:
        """
        Indicates if the pen is currently down.
        
        Returns:
            bool: True if the pen is down, False otherwise.
        """
        return self._pen_down
    
    @property
    def lines(self) -> list:
        """
        Gets the list of lines drawn by the turtle.
        
        Returns:
            list: A list of lines drawn by the turtle, each represented as a pair of Vector objects.
        """
        return list(self._lines)
    
    @position.setter
    def position(self, new_position: Vector) -> None:
        """
        Sets a new position for the turtle.
        
        Parameters:
            new_position (Vector): The new position of the turtle.
        """
        self._position = new_position

    @step.setter
    def step(self, new_step: float) -> None:
        """
        Sets a new step length for the turtle.
        
        Parameters:
            new_step (float): The new step length.
        """
        self._step = new_step

    @angle.setter
    def angle(self, new_angle: float) -> None:
        """
        Sets a new direction for the turtle.
        
        Parameters:
            new_angle (float): The new direction of the turtle in degrees.
        """
        self._angle = (new_angle % 360) * math.pi / 180

    @pen_down.setter
    def pen_down(self, put_pen_down: bool) -> None:
        """
        Sets the pen state.
        
        Parameters:
            put_pen_down (bool): True to put the pen down, False to lift it up.
        """
        self._pen_down = put_pen_down
    
    def clear_lines(self):
        """
        Removes all saved lines. Useful for resetting the turtle's drawing state.
        """
        self._lines.clear()

    def rotate(self, rotate_by: float) -> None:
        """
        Rotates the turtle by a given angle in degrees.
        
        Parameters:
            rotate_by (float): The angle to rotate the turtle by, in degrees.
        """
        self._angle += (rotate_by * math.pi / 180) % (2 * math.pi)

    def forward(self) -> None:
        """
        Moves the turtle forward by the specified distance in its current direction.
        If the pen is down, it draws a line from the previous position to the new position.
        """
        prev = self._position
        self._position += self._step * Vector(math.cos(self._angle), math.sin(self._angle))

        # Recalculate min/max coordinates
        if self._x_min > self._position.x: self._x_min = self._position.x
        if self._y_min > self._position.y: self._y_min = self._position.y
        if self._x_max < self._position.x: self._x_max = self._position.x
        if self._y_max < self._position.y: self._y_max = self._position.y

        if self._pen_down:
            self._lines.append([prev, self._position])
            self._line_drawn(prev, self._position)

    def center_to(self, xc: float, yc: float) -> None:
        """
        Translates all lines (their center) to the specified position.
        
        Parameters:
            xc (float): The x-coordinate of the new center position.
            yc (float): The y-coordinate of the new center position.
        """
        lines_center = Vector((self._x_min + self._x_max) // 2, (self._y_min + self._y_max) // 2)
        translation_vector = Vector(xc, yc) - lines_center

        for line in self._lines:
            line[0] += translation_vector
            line[1] += translation_vector
