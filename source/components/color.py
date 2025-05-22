import colorsys

def hsv_to_hex(h: float, s: float, v: float):
    """
    Convert an HSV color to a hexadecimal string suitable for Tkinter.

    Parameters:
        h (float): Hue component in [0.0, 1.0].
        s (float): Saturation component in [0.0, 1.0].
        v (float): Value (brightness) component in [0.0, 1.0].

    Returns:
        str: Hex color string in the form '#rrggbb'.
    """
    r, g, b = colorsys.hsv_to_rgb(h, s, v)

    return "#{:02x}{:02x}{:02x}".format(
        int(round(r * 255)),
        int(round(g * 255)),
        int(round(b * 255))
    )