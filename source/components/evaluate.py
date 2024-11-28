import math

def evaluate_recursive(data, variables: list[str, float] = {}):
    """
    Evaluates each element in the given input `data` based on the variables defined in the dictionary `variables`.
    
    The function works recursively to process all elements in a structured list.
    
    Parameters:
    data (list, str, int, float, complex):
        Input data, which can be in the form of a string, list, or numerical type (int, float, complex).
        - If the element is of type `str`, it attempts to evaluate it as a mathematical expression using `eval()`.
        - If the element is of type `list`, the function recursively evaluates all its elements.
        - If the element is of type `int`, `float`, or `complex`, it returns it unchanged.
    
    variables (dict):
        A dictionary containing variable names as keys and their corresponding values.
        These variables are used when evaluating strings.
    
    Returns:
    list, int, float, complex, str:
        Returns a list where each element has been recursively evaluated. If an element is of type `str` and is successfully evaluated,
        it returns its numerical value. If the element is a number, it returns it unchanged. If the element is of an unsupported type,
        it returns an error message.
    """

    if isinstance(data, str):
        try:
            return eval(data, {**vars(math)}, variables)
        except Exception as e:
            raise ValueError(f"Error in evaluating expression: {e}")

    elif isinstance(data, list):
        return [evaluate_recursive(element, variables) for element in data]

    elif isinstance(data, (int, float, complex)):
        return data

    else:
        raise ValueError(f"Unsupported type: {type(data)}")