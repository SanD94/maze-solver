import unittest
from maze import Maze
from cell import Wall
from functools import reduce


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
            m1._cells[0][0].wall & Wall.TOP,
            Wall.NONE
        )
        self.assertEqual(
            m1._cells[-1][-1].wall & Wall.BOTTOM,
            Wall.NONE
        )
        visited_all = True
        for i in range(len(m1._cells)):
            for j in range(len(m1._cells[i])):
                visited_all &= m1._cells[i][j].visited
        self.assertEqual(
            visited_all,
            True
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
            m1._cells[0][0].wall & Wall.TOP,
            Wall.NONE,
        )
        self.assertEqual(
            m1._cells[-1][-1].wall & Wall.BOTTOM,
            Wall.NONE
        )

        visited_all = True
        for i in range(len(m1._cells)):
            for j in range(len(m1._cells[i])):
                visited_all &= m1._cells[i][j].visited
        self.assertEqual(
            visited_all,
            True
        )



if __name__ == "__main__":
    unittest.main()