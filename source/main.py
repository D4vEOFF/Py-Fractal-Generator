
import sys
import tkinter as tk
import math
import json

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
    "start_angle": 0,
    "prompt": False
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
        "start_angle": defaults["start_angle"],
        "prompt": defaults["prompt"]
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
        
        # JSON path
        if arg == "-path":
            val = cmd[index + 1]
            args_parsed["path"] = val
        
        # Start angle
        if arg == "-angle":
            val = float(cmd[index + 1])
            args_parsed["start_angle"] = val
        
        # Control-prompting
        if arg == "-prompt":
            args_parsed["prompt"] = True

    
    return args_parsed


def main() -> None:

    window = tk.Tk()

    # Attempt to parse command line arguments
    args = parse_args()

    win_width = args['width']
    win_height = args['height']
    prompt = args["prompt"]

    # Parse JSON
    with open(args["path"]) as f:
        fractal = json.loads(f.read())

    # Display window
    window.geometry(f"{win_width}x{win_height}")
    window.title(f"Fractal Generator - {fractal['name']}")

    canvas=tk.Canvas(window, width=win_width, height=win_height)
    canvas.pack()

    # Turtle
    turtle = Turtle(
        position=Vector(),
        step=args["step"],
        angle=args["start_angle"]
    )
    
    # Load L-system
    lsystem = LSystem(fractal["axiom"], fractal["rules"])
    
    if prompt:
        lsystem.add_iteration_performed_subscriber(lambda word, iteration: print(f"Iteration n. {iteration} string length: {len(word)}"))

    lsystem.iterate(args["iteration_count"])

    angle = fractal["rotateByAngle"]
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

    turtle.center_to(win_width // 2, win_height // 2)

    # Draw figure
    for line in turtle.lines:
        canvas.create_line(line[0].x, line[0].y, line[1].x, line[1].y, fill=args["stroke_color"], width=args["stroke_width"])

    window.mainloop()


if __name__ == '__main__':
    main()