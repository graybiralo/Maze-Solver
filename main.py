from window import Window
from drawing import Point, Line
from cell import Cell
from maze import Maze
if __name__ == "__main__":
    #create window
    win = Window(800, 600)


    maze = Maze(
        x1=50,         # Top-left x-coordinate
        y1=50,         # Top-left y-coordinate
        num_rows=5,    # Number of rows
        num_cols=5,    # Number of columns
        cell_size_x=50,  # Width of each cell
        cell_size_y=50,  # Height of each cell
        win=win        # Reference to the window
    )
    win.wait_for_close()
