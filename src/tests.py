import unittest
from maze import Maze
from cell import Wall


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        self.assertEqual(
            Wall.ALL ^ Wall.TOP,
            m1._cells[0][0].wall
        )
        self.assertEqual(
            Wall.ALL ^ Wall.BOTTOM,
            m1._cells[-1][-1].wall
        )
    
    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        self.assertEqual(
            Wall.ALL ^ Wall.TOP,
            m1._cells[0][0].wall
        )
        self.assertEqual(
            Wall.ALL ^ Wall.BOTTOM,
            m1._cells[-1][-1].wall
        )


if __name__ == "__main__":
    unittest.main()