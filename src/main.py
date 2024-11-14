from window import Window
from cell import Cell, Wall

if __name__ == "__main__":
    win = Window(800, 600)

    c0 = Cell(win)
    c0.wall ^= Wall.LEFT
    c0.draw(50, 50, 100, 100)

    c1 = Cell(win)
    c1.wall ^= Wall.RIGHT
    c1.draw(125, 125, 200, 200)

    c0.draw_move(c1)

    c2 = Cell(win)
    c2.wall ^= Wall.BOTTOM
    c2.draw(225, 225, 250, 250)

    c1.draw_move(c2)

    c3 = Cell(win)
    c3.wall ^= Wall.TOP
    c3.draw(300, 300, 500, 500)

    c2.draw_move(c3, True)

    win.wait_for_close()