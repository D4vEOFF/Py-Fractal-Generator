
import sys
import tkinter as tk
import json
import canvasvg

from components.fractals.fractal import FractalType
from components.fractals.graphics import *
from components.fractals.checker import *

# Default command line argument values
defaults = {
    "width": 1280,
    "height": 720,
    "stroke_color": "black",
    "stroke_width": 3,
    "step": 5,
    "iteration_count": 1,
    "start_angle": 0,
    "prompt": False,
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
        
        # File path
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
        
        # Save to SVG file
        if arg == "-svg-path":
            val = cmd[index + 1]
            args_parsed["svg_path"] = val
    
    return args_parsed


def main() -> None:

    window = tk.Tk()

    # Attempt to parse command line arguments
    args = parse_args()

    win_width = args['width']
    win_height = args['height']
    prompt = args["prompt"]

    # Parse file contents
    file_path = args["path"]
    with open(file_path) as f:
        try:
            fractal = json.loads(f.read())
        except json.JSONDecodeError as err:
            print(err)
            sys.exit(-1)

    # Classify fractal
    fractal_type = FractalType.NONE
    if is_LSystem(fractal):
        fractal_type = FractalType.LSYSTEM
    else: raise KeyError(f"Invalid file format: {file_path}")
    
    # Display window
    window.geometry(f"{win_width}x{win_height}")
    window.title(f"Fractal Generator - {fractal['name']}")

    canvas=tk.Canvas(window, width=win_width, height=win_height)
    canvas.pack()

    # Draw fractal
    if fractal_type == FractalType.LSYSTEM:
        draw_LSystem(fractal, args, canvas)
    
    # Save canvas to SVG
    if 'svg_path' in args.keys():
        canvasvg.saveall(args['svg_path'], canvas)

    window.mainloop()
    sys.exit(0)


if __name__ == '__main__':
    main()