
import math

from ..stack import Stack
from ..vector import Vector
from ..turtle import Turtle
from ..color import hsv_to_hex

from ..fractals.lsystem import LSystem
from ..fractals.ifs import IFS
from ..fractals.tea import TEA

def draw_LSystem(fractal: dict, args: dict, canvas: object) -> None:
    """
    Draws an L-System fractal on a canvas using Turtle graphics.
    
    Parameters:
        fractal (dict): The fractal definition including axiom and rules.
        args (dict): Configuration for drawing, such as step size, start angle, iteration count, etc.
        canvas (object): The canvas where the fractal will be drawn.
    """
    # Turtle
    turtle = Turtle(
        position=Vector(),
        step=args["step"],
        angle=args["start_angle"]
    )
    
    # Load L-system
    lsystem = LSystem(fractal["axiom"], fractal["rules"])
    
    if args["prompt"]:
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

    turtle.center_to(args["window_width"] // 2, args["window_height"] // 2)

    # Draw figure
    for line in turtle.lines:
        canvas.create_line(line[0].x, line[0].y, line[1].x, line[1].y, fill=args["stroke_color"], width=args["stroke_width"])


def draw_IFS(fractal: dict, args: dict, canvas: object) -> None:
    """
    Draws an Iteration Function System (IFS) fractal on a canvas using transformations.
    
    Parameters:
        fractal (dict): The fractal definition including starting figure and mappings.
        args (dict): Configuration for drawing, such as iteration count, scale, start angle, etc.
        canvas (object): The canvas where the fractal will be drawn.
    """
    # Represent all points as vectors
    starting_figure = []
    for point in fractal['starting_figure']:
        starting_figure.append(Vector(point[0], point[1]))

    ifs = IFS(starting_figure, fractal['mappings'])
    ifs.iterate(args['iteration_count'])

    ifs.scale(args['scale'])
    ifs.rotate(180 - args['start_angle'])
    ifs.center_to(args["window_width"] // 2, args["window_height"] // 2)

    result_figures = ifs.figures

    # Plot figures
    figures_listified = []
    for figure in result_figures:
        figure_listified = []
        for point in figure: figure_listified.append(point.as_list)
        figures_listified.append(figure_listified)

    for figure in figures_listified:
        canvas.create_polygon(*[coord for point in figure for coord in point], fill=args['fill_color'], outline=args['stroke_color'])


def draw_TEA(fractal: dict, args: dict, canvas: object) -> None:
    width, height = args['window_width'], args['window_height']
    step = args['step']
    max_iterations = args['iteration_count']
    sequence = fractal['sequence']
    escape_radius = fractal["escape_radius"]
    next_member = fractal['next_member']
    explore_var = fractal['explore_var']
    plot_range = fractal["plot_range"]

    tea = TEA(width, height, sequence, step, escape_radius, tuple(plot_range), next_member, explore_var)
    tea.iterate(max_iterations)
    iter_counts = tea.point_iteration_counts
    final_values = tea.point_last_values

    point_size = step // 2

    # Definice intervalu pro odstín (hue)
    HUE_MIN = 0
    HUE_MAX = 0.87
    SATURATION = 1
    VALUE = 1

    for x in range(len(iter_counts[0])):
        for y in range(len(iter_counts)):
            iterations = iter_counts[y][x]
            if iterations < max_iterations:
                # Bod uniká – použijeme hladké zbarvení
                z = final_values[y][x]
                abs_z = abs(z)
                if abs_z < 1e-10:
                    abs_z = 1e-10
                smooth_iter = iterations + 1 - math.log(math.log(abs_z)) / math.log(2)
                norm = smooth_iter / max_iterations
                hue = HUE_MIN + norm * (HUE_MAX - HUE_MIN)
                hex_color = hsv_to_hex(hue, SATURATION, VALUE)
            else:
                # Bod patří fraktálu – vykreslíme ho černě
                hex_color = "#000000"

            x1 = step * x - point_size
            y1 = step * y - point_size
            x2 = step * x + point_size
            y2 = step * y + point_size
            canvas.create_oval(x1, y1, x2, y2, fill=hex_color, outline="")