
from components.fractals.i_iterable import IFractalIterable
from components.fractals.i_transformable import IFractalTransformable

from components.vector import Vector
from copy import deepcopy
import math

class IFS(IFractalTransformable):
    """
    Iterated Function System (IFS) class for generating fractal transformations.
    """
    def __init__(self, starting_figure: list, tr_coefs: list = []) -> None:
        """
        Initializes an instance of the IFS class.
        
        Parameters:
            starting_figure (list): A list representing the initial set of points in the figure.
            tr_coefs (list): A list of transformation coefficients for generating new figures.
        """
        self._figures = [starting_figure]
        self._total_iterations = 0

        # Min/max coords (used for centering)
        self._x_min, self._y_min, self._x_max, self._y_max = 0, 0, 0, 0
        self.__update_min_max_coords()

        self._transformations = set()
        for tpl in tr_coefs:
            def transformation(point, tpl=deepcopy(tpl)):
                return Vector(
                    tpl[0]*point.x + tpl[1]*point.y + tpl[4],
                    tpl[2]*point.x + tpl[3]*point.y + tpl[5]
                )
            self._transformations.add(transformation)

    @property
    def figures(self) -> list:
        """
        List of all generated figures.
        
        Returns:
            list: A list of figures, each represented by a list of Vector points.
        """
        return list(self._figures)

    def iterate(self, iterations: int) -> None:
        """
        Performs a specified number of iterations.
        
        Parameters:
            iterations (int): The number of iterations to perform.
        """
        for _ in range(iterations):
            figures_new = []
            
            # Apply all transformations on each figure
            for figure in self._figures:
                for tr in self._transformations:
                    figure_new = []
                    for point in figure: figure_new.append(tr(point))

                    figures_new.append(figure_new)
        
            self._figures = figures_new

    def scale(self, factor: float) -> None:
        """
        Scales the figure by a given factor.
        
        Parameters:
            factor (float): The factor by which to scale the figure.
        """
        for figure in self._figures:
            for i in range(len(figure)):
                figure[i] *= factor
        
        self.__update_min_max_coords()

    def translate(self, translation_vector: Vector) -> None:
        """
        Translates the figure by a given vector.
        
        Parameters:
            translation_vector (Vector): The vector by which to translate the figure.
        """
        for figure in self._figures:
            for i in range(len(figure)):
                figure[i] += translation_vector

    def rotate(self, angle: float) -> None:
        """
        Rotates the figure by a given angle (in degrees).
        
        Parameters:
            angle (float): The angle in degrees by which to rotate the figure.
        """
        angle_radians = angle * math.pi / 180

        figure_center = Vector((self._x_min + self._x_max) // 2, (self._y_min + self._y_max) // 2)
        self.translate((-1) * figure_center)

        for figure in self._figures:
            for i in range(len(figure)):
                point = figure[i]
                figure[i] = Vector(
                    point.x * math.cos(angle_radians) - point.y * math.sin(angle_radians),
                    point.x * math.sin(angle_radians) + point.y * math.cos(angle_radians)
                )
        
        self.translate(figure_center)

        self.__update_min_max_coords()

    def center_to(self, xc: float, yc: float) -> None:
        """
        Translates all figures (their center) to a specified position.
        
        Parameters:
            xc (float): The x-coordinate of the new center position.
            yc (float): The y-coordinate of the new center position.
        """
        figure_center = Vector((self._x_min + self._x_max) // 2, (self._y_min + self._y_max) // 2)
        self.translate(Vector(xc, yc) - figure_center)
        self.__update_min_max_coords()

    def __update_min_max_coords(self) -> None:
        """
        Updates the minimum and maximum X and Y coordinates for the figures.
        """
        self._x_min = min(point.x for figure in self._figures for point in figure)
        self._y_min = min(point.y for figure in self._figures for point in figure)
        self._x_max = max(point.x for figure in self._figures for point in figure)
        self._y_max = max(point.y for figure in self._figures for point in figure)
