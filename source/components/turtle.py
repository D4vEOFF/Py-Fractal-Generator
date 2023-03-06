
from components.vector import Vector
from components.event import Event

import math

class Turtle:
    """Turtle 2D graphics."""
    def __init__(self, step: float, position: Vector = Vector(0, 0), angle: float = 0) -> None:
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
        self._line_drawn += method
    def remove_line_drawn_subscriber(self, method):
        self._line_drawn -= method


    @property
    def position(self) -> Vector:
        return Vector(self._position.x, self._position.y)
    
    @property
    def step(self) -> float:
        return self._step
    
    @property
    def angle(self) -> float:
        return self._angle * 180 / math.pi
    
    @property
    def pen_down(self) -> bool:
        return self._pen_down
    
    @property
    def lines(self) -> list:
        return list(self._lines)
    
    @position.setter
    def position(self, new_position: Vector) -> None:
        self._position = new_position

    @step.setter
    def step(self, new_step: float) -> None:
        self._step = new_step

    @angle.setter
    def angle(self, new_angle: float) -> None:
        self._angle = (new_angle % 360) * math.pi / 180

    @pen_down.setter
    def pen_down(self, put_pen_down: bool) -> None:
        self._pen_down = put_pen_down
    
    def clear_lines(self):
        """Removes all saved lines."""
        self._lines.clear()

    def rotate(self, rotate_by):
        """Rotates turtle by a given angle."""
        self._angle += (rotate_by * math.pi / 180) % (2 * math.pi)

    def forward(self) -> None:
        """Moves the turtle forward by specified distance in its current direction."""
        prev = self._position
        self._position += self._step * Vector(math.cos(self._angle), math.sin(self._angle))

        # Recalc min/max coords
        if self._x_min > self._position.x: self._x_min = self._position.x
        if self._y_min > self._position.y: self._y_min = self._position.y
        if self._x_max < self._position.x: self._x_max = self._position.x
        if self._y_max < self._position.y: self._y_max = self._position.y

        if self._pen_down:
            self._lines.append([prev, self._position])
            self._line_drawn(prev, self._position)

    def center_to(self, xc: float, yc: float) -> None:
        """Translates all lines (their center) to specified position."""
        lines_center = Vector((self._x_min + self._x_max) // 2, (self._y_min + self._y_max) // 2)
        translation_vector = Vector(xc, yc) - lines_center

        for line in self._lines:
            line[0] += translation_vector
            line[1] += translation_vector