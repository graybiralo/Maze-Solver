import unittest
from maze import Maze
from window import Window
class Tests(unittest.TestCase):
    #maze
    def test_maze_creation(self):
        num_rows = 5
        num_cols = 4
        cell_size_x = 10
        cell_size_y = 10
        maze = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y)

        
        self.assertEqual(len(maze._cells), num_rows)
        self.assertEqual(len(maze._cells[0]), num_cols)

        
        cell = maze._cells[0][0]
        self.assertIsNotNone(cell)
        self.assertEqual(cell._x1, 0)
        self.assertEqual(cell._y1, 0)

    
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        
        self.assertEqual(len(m1._cells), num_rows)


        self.assertEqual(len(m1._cells[0]), num_cols)

    #cell
    def test_break_entrance_and_exit(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 20, 20)

        # Break the entrance and exit walls
        m1._break_entrance_and_exit()

        # Check top-left cells top wall
        self.assertFalse(m1._cells[0][0].has_top_wall)

        # Check bottom-right cells bottom wall
        self.assertFalse(m1._cells[num_rows - 1][num_cols - 1].has_bottom_wall)


class TestMaze(unittest.TestCase):
    def test_reset_cells_visited(self):
        # Create a small test maze
        win = Window(800, 600)
        maze = Maze(
            x1=0, y1=0,
            num_rows=3, num_cols=3,
            cell_size_x=50, cell_size_y=50,
            win=win
        )
        
        # Mark all cells as visited
        for row in maze._cells:
            for cell in row:
                cell.visited = True

        # Call the method to reset visited
        maze._reset_cells_visited()

        # Check that all cells visited property is False
        for row in maze._cells:
            for cell in row:
                self.assertFalse(cell.visited, "Cell visited property should be False after reset")

        print("Test passed: All cells' visited properties reset successfully.")


if __name__ == "__main__":
    unittest.main()
