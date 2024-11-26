
from components.fractals.i_iterable import IFractalIterable
from components.vector import Vector
from copy import deepcopy

class IFS(IFractalIterable):
    """Iteration Function System"""
    def __init__(self, starting_figure: list, tr_coefs: list = []) -> None:
        self._figures = [starting_figure]
        self._total_iterations = 0

        self._transformations = set()
        for tpl in tr_coefs:
            # print(tpl)
            def transformation(point, tpl=deepcopy(tpl)):
                return Vector(
                    tpl[0]*point.x + tpl[1]*point.y + tpl[4],
                    tpl[2]*point.x + tpl[3]*point.y + tpl[5]
                )
            self._transformations.add(transformation)

    
    @property
    def figures(self) -> list:
        return list(self._figures)
    
    
    def iterate(self, iterations) -> None:

        for _ in range(iterations):
            figures_new = []
            # Apply all transformations on each figure
            for figure in self._figures:
                for tr in self._transformations:
                    figure_new = []
                    # print(figure_new)
                    for point in figure: figure_new.append(tr(point))
                    figures_new.append(figure_new)
        
            self._figures = figures_new
    

    def center_to(self, xc: float, yc: float) -> None:
        """Translates all figures (their center) to specified position."""
        