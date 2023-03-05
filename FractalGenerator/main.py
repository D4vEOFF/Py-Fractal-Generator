
import sys
import tkinter as tk

from components.turtle import Turtle
from components.vector import Vector


def parse_args(width_default: int, height_default: int, stroke_color_default: str, stroke_width_default: int, step_default: int) -> dict:
    """Parses command line arguments."""
    args_parsed = {
        "width": width_default,
        "height": height_default,
        "stroke_color": stroke_color_default,
        "stroke_width": stroke_width_default,
        "step": step_default
    }
    cmd = sys.argv

    for index, arg in enumerate(cmd):
        # Window width
        if arg == "-w":
            val = int(cmd[index + 1])
            if val <= 0:
                raise ValueError("Window resolution must be a pair of positive values.")
            args_parsed["width"] = val
        
        # Window height
        if arg == "-h":
            val = int(cmd[index + 1])
            if val <= 0:
                raise ValueError("Window resolution must be a pair of positive values.")
            args_parsed["height"] = val
        
        # Stroke color
        if arg == "-sc":
            val = cmd[index + 1]
            args_parsed["stroke_color"] = val
        
        # Stroke width
        if arg == "-sw":
            val = int(cmd[index + 1])
            if val <= 0:
                raise ValueError("Stroke width must be a positive integer.")
            args_parsed["stroke_width"] = val
        
        if arg == "-step":
            val = int(cmd[index + 1])
            if val <= 0:
                raise ValueError("Step must be a positive integer.")
            args_parsed["step"] = val
    
    return args_parsed


def main() -> None:

    window = tk.Tk()

    # Attempt to parse command line arguments
    args = parse_args(1280, 720, "black", 3, 50)

    win_width = args['width']
    win_height = args['height']

    # Display window
    window.geometry(f"{win_width}x{win_height}")

    canvas=tk.Canvas(window, width=win_width, height=win_height)
    canvas.pack()

    # Turtle
    turtle = Turtle(
        position=Vector(win_width // 2, win_height - 10),
        step=args['step'],
        angle=0
    )
    turtle.add_line_drawn_subscriber(
        lambda prevPos, newPos :
            canvas.create_line(prevPos.x, prevPos.y, newPos.x, newPos.y, fill=args['stroke_color'], width=args['stroke_width'])
    )

    turtle.pen_down = True
    turtle.forward()

    window.mainloop()


if __name__ == '__main__':
    main()