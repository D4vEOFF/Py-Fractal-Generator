
from components.fractals.i_iterable import IFractalIterable

class IFS(IFractalIterable):
    """Iteration Function System"""
    def __init__(self, starting_figure: list, tr_coefs: list = []) -> None:
        self._figures = [starting_figure]
        self._total_iterations = 0

        self._transformations = set()
        for tpl in tr_coefs:
            self._transformations.append(
                lambda p: [
                    tpl[0]*p[0] + tpl[1]*p[1] + tpl[4],
                    tpl[2]*p[0] + tpl[3]*p[1] + tpl[5]
                ]
            )

    
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
                    for point in figure: figure_new.append(tr(point))
                    figures_new.append(figure_new)
        
        self._figures = figures_new