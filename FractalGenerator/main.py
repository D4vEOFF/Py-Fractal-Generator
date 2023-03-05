
import sys
import tkinter as tk


def parse_args(width_default: int, height_default: int) -> dict:
    """Parses command line arguments."""
    args_parsed = {
        "width": width_default,
        "height": height_default
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
    
    return args_parsed


def main() -> None:

    window = tk.Tk()

    mon_width = window.winfo_screenwidth()
    mon_height = window.winfo_screenheight()

    # Attempt to parse command line arguments
    args = parse_args(1280, 720)

    # TODO: implement TKinter window display


if __name__ == '__main__':
    main()