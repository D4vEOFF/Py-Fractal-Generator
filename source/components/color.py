import colorsys

def hsv_to_hex(h: int, s: int, v: int):
    """Převod HSV na hexadecimální formát pro Tkinter."""
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return f"#{int(r * 255):02x}{int(g * 255):02x}{int(b * 255):02x}"