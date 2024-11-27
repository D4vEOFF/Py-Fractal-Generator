
from ..stack import Stack
from ..vector import Vector
from ..turtle import Turtle

from ..fractals.lsystem import LSystem
from ..fractals.ifs import IFS

def draw_LSystem(fractal: dict, args: dict, canvas: object) -> None:
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


def draw_IFS(fractal: dict, args: dict, canvas: object):

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