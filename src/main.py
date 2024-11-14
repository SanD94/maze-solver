from window import Window
from drawing_utils import Line, Point

if __name__ == "__main__":
    win = Window(800, 600)
    line0 = Line(Point(100.1, 200.2), Point(200.2, 200.2))
    line1 = Line(Point(200.2, 200.2), Point(200.2, 300.6))
    win.draw_line(line0, "black")
    win.draw_line(line1, "red")

    win.wait_for_close()