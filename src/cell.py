from drawing_utils import Line, Point
from window import Window
from enum import Flag


class Wall(Flag):
    TOP = 1
    RIGHT = 2
    BOTTOM = 4
    LEFT = 8
    ALL = 15
    NONE = 0


class Cell:
    def __init__(self, win : Window | None = None):
        self._x1 = None 
        self._x2 = None 
        self._y1 = None 
        self._y2 = None 
        self._win = win
        self.wall = Wall.ALL
        
    def draw(self, x1 : float, y1 : float, x2 : float, y2 : float):
        if self._win is None:
            return
        # x1, y1 left top
        # x2, y2 right bottom
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        
        walls = [Wall.TOP, Wall.RIGHT, Wall.BOTTOM, Wall.LEFT]
        points = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]

        for i, wall in enumerate(walls):
            if self.wall & wall:
                start = points[i]
                end = points[(i+1) % 4]
                cur_line = Line(Point(*start), Point(*end))
                self._win.draw_line(cur_line)
        
    def draw_move(self, to_cell : 'Cell', undo : bool = False):
        center = self._get_center()
        to_cell_center = to_cell._get_center()
        color = "gray" if undo else "red"
        self._win.draw_line(Line(center, to_cell_center), color)

    def _get_center(self):
        return Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)