from window import Window
from cell import Cell, Wall

if __name__ == "__main__":
    win = Window(800, 600)

    c = Cell(win)
    c.wall ^= Wall.LEFT
    c.draw(50, 50, 100, 100)

    c = Cell(win)
    c.wall ^= Wall.RIGHT
    c.draw(125, 125, 200, 200)

    c = Cell(win)
    c.wall ^= Wall.BOTTOM
    c.draw(225, 225, 250, 250)

    c = Cell(win)
    c.wall ^= Wall.TOP
    c.draw(300, 300, 500, 500)

    win.wait_for_close()