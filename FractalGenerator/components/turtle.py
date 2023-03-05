
from vector import Vector
from math import sin, cos

class Turtle:
    """Turtle 2D graphics."""
    def __init__(self, step: float, position: Vector = Vector(0, 0), angle: float = 0) -> None:
        self._position = position
        self._step = step
        self._angle = angle
        self._pen_down = False

    @property
    def position(self) -> Vector:
        return self._position
    
    @property
    def step(self) -> float:
        return self._step
    
    @property
    def angle(self) -> float:
        return self._angle
    
    @property
    def pen_down(self) -> bool:
        return self._pen_down
    
    @position.setter
    def position(self, new_position: Vector) -> None:
        self._position = new_position

    @step.setter
    def step(self, new_step: float) -> None:
        self._step = new_step

    @angle.setter
    def angle(self, new_angle: float) -> None:
        self._angle = new_angle

    @pen_down.setter
    def pen_down(self, put_pen_down: bool) -> None:
        self._pen_down = put_pen_down
    
    def forward(self) -> None:
        """Moves the turtle forward by specified distance in its current direction."""
        self._position += self._step * Vector(cos(self._angle), sin(self._angle))