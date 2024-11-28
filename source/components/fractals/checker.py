from ..fractals.fractal import FractalType

lsystem_keys = ["name", "axiom", "rules", "rotateByAngle"]
ifs_keys = ["name", "starting_figure", "mappings"]

def determine_fractal_type(fractal: dict) -> FractalType:
    """
    Determines the type of fractal based on the keys present in the dictionary.
    
    Args:
        fractal (dict): Dictionary containing fractal definition.
        
    Returns:
        FractalType: The type of the fractal (LSYSTEM, IFS) or None if not recognized.
    
    Raises:
        ValueError: If the fractal dictionary does not match any known fractal type structure or if required values are of incorrect types.
    """
    # Check for L-System specific structure
    if all(key in fractal.keys() for key in lsystem_keys):
        if not isinstance(fractal.get("name"), str):
            raise ValueError("L-System error: 'name' must be a string.")
        if not isinstance(fractal.get("axiom"), str):
            raise ValueError("L-System error: 'axiom' must be a string.")
        if not isinstance(fractal.get("rules"), dict):
            raise ValueError("L-System error: 'rules' must be a dictionary.")
        if not all(isinstance(rule_key, str) and isinstance(rule_value, str) for rule_key, rule_value in fractal["rules"].items()):
            raise ValueError("L-System error: All keys and values in 'rules' must be strings.")
        if not isinstance(fractal.get("rotateByAngle"), (float, int)):
            raise ValueError("L-System error: 'rotateByAngle' must be a float or an int.")
        return FractalType.LSYSTEM
    # Check for IFS specific structure
    elif all(key in fractal.keys() for key in ifs_keys):
        if not isinstance(fractal.get("name"), str):
            raise ValueError("IFS error: 'name' must be a string.")
        if not isinstance(fractal.get("starting_figure"), list):
            raise ValueError("IFS error: 'starting_figure' must be a list of pairs of floats or ints.")
        if not all(isinstance(pair, list) and len(pair) == 2 and all(isinstance(value, (float, int)) for value in pair) for pair in fractal["starting_figure"]):
            raise ValueError("IFS error: Each element in 'starting_figure' must be a list of two floats or ints.")
        if not isinstance(fractal.get("mappings"), list):
            raise ValueError("IFS error: 'mappings' must be a list of lists of six floats or ints.")
        if not all(isinstance(mapping, list) and len(mapping) == 6 and all(isinstance(value, (float, int)) for value in mapping) for mapping in fractal["mappings"]):
            raise ValueError("IFS error: Each element in 'mappings' must be a list of six floats or ints.")
        return FractalType.IFS
    else:
        raise ValueError("The provided fractal dictionary does not match any known fractal type structure.")
