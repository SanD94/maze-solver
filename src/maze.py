from cell import Cell
from window import Window
from time import sleep

class Maze:
    def __init__(
            self,
            x1 : float, y1 : float,
            num_rows : int, num_cols : int,
            cell_size_x : float, cell_size_y : float,
            win : Window
        ):
        if win is None:
            raise ValueError("There is no window to render!")
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
    
    def _create_cells(self):
        self._cells : list[list[Cell]] = []

        for i in range(self._num_rows):
            cur_col : list[Cell] = []
            for j in range(self._num_cols):
                cell = Cell(self._win)
                cur_col.append(cell)
            self._cells.append(cur_col)
        
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i : int, j : int):
        ## x1 y1 left top
        ## x2 y2 right bottom
        x1 = self._x1 + self._cell_size_x * i
        x2 = self._x1 + self._cell_size_x * (i + 1)
        y1 = self._y1 + self._cell_size_y * j
        y2 = self._y1 + self._cell_size_y * (j + 1)
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        sleep(0.05)
        
