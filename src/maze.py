from cell import Cell, Wall
from window import Window
from time import sleep
import random

class Maze:
    def __init__(
            self,
            x1 : float, y1 : float,
            num_rows : int, num_cols : int,
            cell_size_x : float, cell_size_y : float,
            win : Window | None = None,
            seed : int | None = None
        ):
        
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._random = random.Random(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        
    
    def _create_cells(self):
        self._cells : list[list[Cell]] = []

        for i in range(self._num_cols):
            cur_col : list[Cell] = []
            for j in range(self._num_rows):
                cell = Cell(self._win)
                cur_col.append(cell)
            self._cells.append(cur_col)
        
        for i in range(self._num_cols):
            for j in range(self._num_rows):
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

    def _break_entrance_and_exit(self):
        self._cells[0][0].wall ^= Wall.TOP
        self._cells[-1][-1].wall ^= Wall.BOTTOM

        self._draw_cell(0, 0)
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    # i col, j row
    def _break_walls_r(self, i : int, j : int):
        self._cells[i][j].visited = True
        adjs = [(0,-1), (1,0), (0,1), (-1,0)]
        walls = [Wall.TOP, Wall.RIGHT, Wall.BOTTOM, Wall.LEFT]
    
        while True:
            to_visit : list[tuple[int, int, int]] = []
            for index, adj in enumerate(adjs):
                n_i, n_j = i + adj[0], j + adj[1]
                if  (
                    0 <= n_i and n_i < self._num_cols and
                    0 <= n_j and n_j < self._num_rows and
                    not self._cells[n_i][n_j].visited
                    ):
                    to_visit.append((n_i, n_j, index))
            if to_visit == []:
                self._draw_cell(i, j)
                return
            visit_index = self._random.randrange(len(to_visit))
            n_i, n_j, wall_index = to_visit[visit_index]
            self._cells[i][j].wall ^= walls[wall_index]
            self._cells[n_i][n_j].wall ^= walls[(wall_index + 2) % 4]

            self._break_walls_r(n_i, n_j)

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False
        

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.05)

    def solve(self):
        return self._solve(0, 0)
    
    def _solve(self, i : int, j : int):
        self._animate()
        self._cells[i][j].visited = True
        if (
            i == self._num_cols - 1 and 
            j == self._num_rows - 1
        ):
            return True
        adjs = [(0,-1), (1,0), (0,1), (-1,0)]
        walls = [Wall.TOP, Wall.RIGHT, Wall.BOTTOM, Wall.LEFT]
        for index, adj in enumerate(adjs):
            n_i, n_j = i + adj[0], j + adj[1]
            if  (
                0 <= n_i and n_i < self._num_cols and
                0 <= n_j and n_j < self._num_rows and
                (self._cells[i][j].wall & walls[index] is Wall.NONE) and
                not self._cells[n_i][n_j].visited
                ):
                self._cells[i][j].draw_move(self._cells[n_i][n_j])
                val = self._solve(n_i, n_j)
                if val:
                    return True
                self._cells[i][j].draw_move(self._cells[n_i][n_j], True)
        return False
                
        

        
