
from ..fractals.fractal import FractalType


lsystem_keys = ["name", "axiom", "rules", "rotateByAngle"]
ifs_keys = ["name", "starting_figure", "mappings"]

def _contains_proper_keys(fractal: dict, fractal_type: int):

    key_presence = None
    if fractal_type == FractalType.LSYSTEM:
        key_presence = [key in fractal.keys() for key in lsystem_keys]
    elif fractal_type == FractalType.IFS:
        key_presence = [key in fractal.keys() for key in ifs_keys]
    
    # Key is missing
    if False in key_presence:
        return False
    
    return True


def is_LSystem(fractal: dict) -> bool:
    """Checks whether given dictionary contains proper keys specific for LSystem."""
    return _contains_proper_keys(fractal, FractalType.LSYSTEM)


def is_IFS(fractal: dict) -> bool:
    """Checks whether given dictionary contains proper keys specific for IFS."""
    return _contains_proper_keys(fractal, FractalType.IFS)