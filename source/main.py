import argparse
import sys
import tkinter as tk
import json
import canvasvg

from components.fractals.fractal import FractalType
from components.fractals.graphics import *
from components.fractals.checker import *


# Default command line argument values
def parse_console_arguments() -> dict:
    """
    Parses command line arguments for the fractal generator application.

    Returns:
        dict: A dictionary containing the parsed command line arguments.
    """
    parser = argparse.ArgumentParser(description="Fractal Generator Arguments")
    
    # Arguments definition
    parser.add_argument("-ww", "--window-width", type=int, default=1280, help="Window width (default: 1280)")
    parser.add_argument("-wh", "--window-height", type=int, default=720, help="Window height (default: 720)")
    parser.add_argument("-sc", "--stroke-color", type=str, default="black", help="Stroke color (default: black)")
    parser.add_argument("-sw", "--stroke-width", type=int, default=3, help="Stroke width (default: 3)")
    parser.add_argument("-fc", "--fill-color", type=str, default='red', help="Fill color (default: red)")
    parser.add_argument("-step", type=int, default=5, help="Step size (default: 5)")
    parser.add_argument("-scale", type=int, default=1, help="Plot scale (default: 1)")
    parser.add_argument("-iter", "--iteration-count", type=int, default=1, help="Iteration count (default: 1)")
    parser.add_argument("-angle", "--start-angle", type=float, default=0, help="Start angle (default: 0)")
    parser.add_argument("-prompt", action="store_true", help="Enable prompt mode")
    parser.add_argument("-path", type=str, help="File path to fractal JSON definition")
    parser.add_argument("-svg-path", type=str, help="Path to save SVG output")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Convert Namespace to dictionary
    return vars(args)


def main() -> None:
    """
    Main function to initialize the fractal generator application.

    It creates a Tkinter window, parses command line arguments, loads fractal data from a file,
    determines the fractal type, and draws the fractal on a Tkinter canvas.
    """
    window = tk.Tk()

    # Attempt to parse command line arguments
    args = parse_console_arguments()

    win_width = args['window_width']
    win_height = args['window_height']
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
    try:
        fractal_type = determine_fractal_type(fractal)
    except ValueError as err:
        print(err)
        sys.exit(-1)
    
    # Display window
    window.geometry(f"{win_width}x{win_height}")
    window.title(f"Fractal Generator - {fractal['name']}")

    canvas=tk.Canvas(window, width=win_width, height=win_height)
    canvas.pack()

    # Draw fractal
    if fractal_type == FractalType.LSYSTEM:
        draw_LSystem(fractal, args, canvas)
    elif fractal_type == FractalType.IFS:
        draw_IFS(fractal, args, canvas)
    
    # Save canvas to SVG
    if args['svg_path'] is not None:
        canvasvg.saveall(args['svg_path'], canvas)

    window.mainloop()
    sys.exit(0)


if __name__ == '__main__':
    main()
