
class LSystem:

    def __init__(self, start_symbol: str, rules: dict) -> None:
        self._word = start_symbol
        self._rules = rules
        self._total_iterations = 0

    
    @property
    def word(self):
        return self._word
    
    @property
    def rules(self):
        return self._rules
    
    @property
    def total_iterations(self):
        return self._total_iterations
    
    
    def iterate(self, iteration_count):
        for _ in range(iteration_count):
            self._word = self._word.translate(str.maketrans(self._rules))
            self._total_iterations += 1