
import sys
import tkinter as tk
import math

from components.turtle import Turtle
from components.vector import Vector
from components.stack import Stack

from components.fractals.lsystem import LSystem

# Default command line argument values
defaults = {
    "width": 1280,
    "height": 720,
    "stroke_color": "black",
    "stroke_width": 3,
    "step": 50,
    "iteration_count": 1,
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
        angle=-90
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
    
    # Load L-system
    lsystem = LSystem("F", {
        "F": "→F[+F]F[-F]F",
    })
    
    lsystem.iterate(args["iteration_count"])

    angle = 25.7
    stack = Stack()
    for char in lsystem.word:
        if char == '+':
            turtle.rotate(angle)
        elif char == '-':
            turtle.rotate(-angle)
        elif char == 'f':
            turtle.pen_down = False
            turtle.forward()
        elif char == '[':
            stack.push((turtle.position, turtle.angle))
        elif char == ']':
            state = stack.pop()
            turtle.position = state[0]
            turtle.angle = state[1]
        else:
            turtle.pen_down = True
            turtle.forward()

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