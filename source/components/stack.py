from copy import deepcopy

class Stack:
    """Represents a pushdown stack."""
    def __init__(self, items: list = []) -> None:
        """
        Initializes a new instance of the Stack class.
        
        Parameters:
            items (list): An optional list of initial items in the stack. Defaults to an empty list.
        """
        self._items = items
    
    @property
    def items(self):
        """
        Gets a copy of the items currently in the stack.
        
        Returns:
            list: A copy of the list containing the items in the stack.
        """
        return deepcopy(self._items)

    def push(self, item: object) -> None:
        """
        Pushes a new element to the stack.
        
        Parameters:
            item (object): The item to be pushed onto the stack.
        """
        self._items.insert(0, item)
    
    def pop(self) -> object:
        """
        Pops an element off the top of the stack.
        
        Returns:
            object: The item that was at the top of the stack.
        """
        item = self._items[0]
        del self._items[0]
        return item

    def __len__(self) -> int:
        """
        Gets the number of items currently in the stack.
        
        Returns:
            int: The number of items in the stack.
        """
        return len(self._items)
