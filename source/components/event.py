class Event(object):
    """
    Represents a simple event system that allows handlers (functions) to be registered, removed, and called.
    """
    
    def __init__(self):
        """
        Initializes a new instance of the Event class.
        """
        self.__eventhandlers = []
 
    def __iadd__(self, handler):
        """
        Adds an event handler to the list of handlers.
        
        Parameters:
            handler (function): The function to be called when the event is triggered.
        
        Returns:
            Event: The updated event instance with the new handler.
        """
        self.__eventhandlers.append(handler)
        return self
 
    def __isub__(self, handler):
        """
        Removes an event handler from the list of handlers.
        
        Parameters:
            handler (function): The function to be removed from the event.
        
        Returns:
            Event: The updated event instance with the handler removed.
        """
        self.__eventhandlers.remove(handler)
        return self
 
    def __call__(self, *args, **keywargs):
        """
        Calls all registered event handlers with the given arguments.
        
        Parameters:
            *args: Positional arguments to be passed to each handler.
            **keywargs: Keyword arguments to be passed to each handler.
        """
        for eventhandler in self.__eventhandlers:
            eventhandler(*args, **keywargs)
