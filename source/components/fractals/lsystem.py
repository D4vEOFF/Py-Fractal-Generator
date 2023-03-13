
from ..event import Event

class LSystem:

    def __init__(self, start_symbol: str, rules: dict) -> None:
        self._word = start_symbol
        self._rules = rules
        self._total_iterations = 0

        self._iteration_performed = Event()

    
    def add_iteration_performed_subscriber(self, method) -> None:
        self._iteration_performed += method

    def remove_iteration_performed_subscriber(self, method) -> None:
        self._iteration_performed -= method

    @property
    def word(self):
        """Current string."""
        return self._word
    
    @property
    def rules(self):
        """Set of rules applied to generate new iteration."""
        return self._rules
    
    @property
    def total_iterations(self):
        return self._total_iterations
    
    
    def iterate(self, iteration_count):
        """Performs specified number of iterations upon the current string."""
        for _ in range(iteration_count):
            self._word = self._word.translate(str.maketrans(self._rules))
            self._total_iterations += 1
            self._iteration_performed(self._word, self._total_iterations)