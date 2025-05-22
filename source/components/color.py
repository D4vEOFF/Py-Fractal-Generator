import colorsys

def hsv_to_hex(h: float, s: float, v: float):
    """Převod HSV na hexadecimální formát pro Tkinter."""
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