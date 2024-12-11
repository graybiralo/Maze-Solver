from window import Window
from maze import Maze
from tkinter import messagebox  # For popup dialogs
import tkinter as tk

def main():
    # Create the window
    win = Window(1920, 1080)  

    # Initialize the maze
    maze = Maze(
        x1=50,         # Top-left x-coordinate
        y1=60,         # Top-left y-coordinate
        num_rows=5,    # Number of rows
        num_cols=5,    # Number of columns
        cell_size_x=100,  # Width of each cell
        cell_size_y=100,  # Height of each cell
        win=win        # Reference to the window
    )

    # Generate the maze
    maze._break_entrance_and_exit()
    maze._break_walls()

    # Solve the maze
    solved = maze.solve()

    # Show result popup
    root = tk.Tk()
    root.withdraw() 
    if solved:
        result = messagebox.askyesno("Maze Solved", "Maze solved successfully!\nDo you want to reload?")

    # Reload or exit based on user's choice
    if result:
        win.close()  # Close the current window
        main()       # Restart the main function to reload the maze
    else:
        win.close()  # Close the window

if __name__ == "__main__":
    main()
