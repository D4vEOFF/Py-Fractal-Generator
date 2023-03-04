
from PyQt6.QtWidgets import QApplication, QLabel, QWidget
import screeninfo
import sys


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

    # Get primary monitor resolution
    for monitor in screeninfo.get_monitors():
        if not monitor.is_primary:
            continue

        mon_width = monitor.width
        mon_height = monitor.height
        break

    # Attempt to parse command line arguments
    args = parse_args(1280, 720)

    # Display window
    app = QApplication([])

    window = QWidget()
    window.setWindowTitle("PyQt App")
    window.setGeometry(
        (mon_width - args["width"]) // 2,
        (mon_height - args["height"]) // 2,
        args["width"],
        args["height"])
    helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
    helloMsg.move(0, 0)

    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()