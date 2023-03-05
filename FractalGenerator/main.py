
import sys
import tkinter as tk
import math

from components.turtle import Turtle
from components.vector import Vector

from components.fractals.lsystem import LSystem

# Default command line argument values
defaults = {
    "width": 1280,
    "height": 720,
    "stroke_color": "black",
    "stroke_width": 3,
    "step": 50,
    "iteration_count": 1,
    "angle": 90
}

def parse_args() -> dict:
    """Parses command line arguments."""
    args_parsed = {
        "width": defaults["width"],
        "height": defaults["height"],
        "stroke_color": defaults["stroke_color"],
        "stroke_width": defaults["stroke_width"],
        "step": defaults["step"],
        "iteration_count": defaults["iteration_count"],
        "angle": defaults["angle"]
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
        
        # Turtle step
        if arg == "-step":
            val = int(cmd[index + 1])
            if val <= 0:
                raise ValueError("Step must be a positive integer.")
            args_parsed["step"] = val
        
        # Iteration count
        if arg == "-iter":
            val = int(cmd[index + 1])
            if val < 0:
                raise ValueError("Iteration count must be a positive integer.")
            args_parsed["iteration_count"] = val
        
        # Rotation angle
        if arg == "-angle":
            val = float(cmd[index + 1])
            if val <= 0:
                raise ValueError("Rotation angle must be a float value.")
            args_parsed["angle"] = val
    
    return args_parsed


def main() -> None:

    window = tk.Tk()

    # Attempt to parse command line arguments
    args = parse_args()

    win_width = args['width']
    win_height = args['height']

    # Display window
    window.geometry(f"{win_width}x{win_height}")

    canvas=tk.Canvas(window, width=win_width, height=win_height)
    canvas.pack()

    # Turtle
    turtle = Turtle(
        position=Vector(2 * win_width // 3, win_height - 10),
        step=args['step'],
        angle=180
    )

    lines = []
    x_min, y_min = math.inf, math.inf
    x_max, y_max = -math.inf, -math.inf
    def on_forward(prevPos, newPos):
        nonlocal x_min, x_max, y_min, y_max
        m_x = min(prevPos.x, newPos.x)
        m_y = min(prevPos.y, newPos.y)
        M_x = max(prevPos.x, newPos.x)
        M_y = max(prevPos.y, newPos.y)

        if x_min > m_x: x_min = m_x
        if y_min > m_y: y_min = m_y
        if x_max < M_x: x_max = M_x
        if y_max < M_y: y_max = M_y

        lines.append([prevPos, newPos])

    turtle.add_line_drawn_subscriber(on_forward)

    turtle.pen_down = True
    
    # Debug
    lsystem = LSystem("R", {
        "L": "R+L+R",
        "R": "L-R-L"
    })
    
    lsystem.iterate(args["iteration_count"])

    angle = args["angle"]
    for char in lsystem.word:
        if char == '+':
            turtle.rotate(angle)
        elif char == '-':
            turtle.rotate(-angle)
        else: turtle.forward()

    # Center figure
    center = Vector((x_min + x_max) // 2, (y_min + y_max) // 2)
    translation_vector = Vector(win_width // 2, win_height // 2) - center

    for line in lines:
        line[0] += translation_vector
        line[1] += translation_vector

    # Draw figure
    for line in lines:
        canvas.create_line(line[0].x, line[0].y, line[1].x, line[1].y, fill=args["stroke_color"], width=args["stroke_width"])

    window.mainloop()


if __name__ == '__main__':
    main()