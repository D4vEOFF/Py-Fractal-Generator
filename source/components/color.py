import colorsys

def hsv_to_hex(h: float, s: float, v: float):
    """
    Convert an HSV color to a hexadecimal string suitable for Tkinter.

    Parameters:
        h (float): Hue component. Either in [0.0, 1.0] or [0, 360] degrees.
        s (float): Saturation component. Either in [0.0, 1.0] or [0, 100] percent.
        v (float): Value (brightness) component. Either in [0.0, 1.0] or [0, 100] percent.

    Returns:
        str: Hex color string in the form '#rrggbb'.
    """
    if 0.0 <= h <= 1.0 and 0.0 <= s <= 1.0 and 0.0 <= v <= 1.0:
        h_norm, s_norm, v_norm = h, s, v
    else:
        h_norm = (h % 360) / 360.0
        s_norm = max(0.0, min(s, 100.0)) / 100.0
        v_norm = max(0.0, min(v, 100.0)) / 100.0

    r, g, b = colorsys.hsv_to_rgb(h_norm, s_norm, v_norm)

    return "#{:02x}{:02x}{:02x}".format(
        int(round(r * 255)),
        int(round(g * 255)),
        int(round(b * 255))
    )