
from copy import deepcopy

class Stack:
    """Represents a pushdown stack."""
    def __init__(self, items: list = []) -> None:
        self._items = items
    
    @property
    def items(self):
        return deepcopy(self._items)

    def push(self, item: object) -> None:
        """Pushes new element to the stack."""
        self._items.insert(0, item)
    
    def pop(self) -> object:
        """Pops an element off top of stack."""
        item = self._items[0]
        del self._items[0]
        return item


    def __len__(self) -> int:
        return len(self._items)