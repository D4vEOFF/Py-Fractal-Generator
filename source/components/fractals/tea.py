
import math

from components.fractals.i_iterable import IFractalIterable
from components.fractals.i_transformable import IFractalTransformable
from components.vector import Vector

class TEA(IFractalIterable, IFractalTransformable):
    
    def __init__(self, width: int, height: int, sequence: str, step: int = 1, escape_radius: int = 2, bounds: tuple = (-2, 2, -2, 2), var: str = 'z', explore_var: str = 'c'):
        self._x_count, self._y_count = width // step, height // step
        
        self._iter_counts = [[0 for _ in range(self._x_count)] for _ in range(self._y_count)]
        self._width, self._height = width, height
        self._sequence = sequence
        self._var = var
        self._explore_var = explore_var
        self._total_iterations = 0
        self._escape_radius = escape_radius

        x_min, x_max, y_min, y_max = bounds

        x_vals = [x_min + step * (x_max - x_min) * j / width for j in range(self._x_count + 1)]
        y_vals = [y_min + step * (y_max - y_min) * i / height for i in range(self._y_count + 1)]
        self._complex_grid = [[x + 1j * y for x in x_vals] for y in y_vals]

        self.point_last_values = [[0 for _ in range(self._x_count)] for _ in range(self._y_count)]

    @property
    def total_iterations(self):
        """
        Returns the total number of iterations performed.
        
        Returns:
            int: Total number of iterations.
        """
        return self._total_iterations
    
    @property
    def point_iteration_counts(self):
        """
        Returns a list of numbers stating how many iterations it took for each point to diverge.

        Returns:
            list: List of iteration counts for each point.
        """
        return list(self._iter_counts)
    
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
    
    def iterate(self, iterations: int) -> None:
        """
        Performs a specified number of iterations.
        
        Parameters:
            iterations (int): The number of iterations to perform.
        """
        
        self._iter_counts = [[0 for _ in range(self._x_count)] for _ in range(self._y_count)]
        self._total_iterations += iterations

        # equation_compiled = compile(self._sequence, '<string>', 'eval')

        for i in range(self._y_count):
            for j in range(self._x_count):
                # Initialize variables
                vars_dict = {self._var: 0, self._explore_var: self._complex_grid[i][j]}

                # Iterate
                for k in range(1, iterations + 1):
                    try:
                        # Evaluate the next value in the sequence
                        vars_dict[self._var] = eval(self._sequence, {"math": math}, vars_dict)

                        # Check for escape condition
                        self._iter_counts[i][j] = k
                        if abs(vars_dict[self._var]) > self._escape_radius:
                            break
                    except OverflowError:
                        self._iter_counts[i][j] = k
                        break
                
                self.point_last_values[i][j] = vars_dict[self._var]