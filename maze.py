from cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win= None, seed = None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._cells = []

        if seed is not None:
            random.seed(seed)
        
        self._create_cells()

    
    def _create_cells(self):
        for i in range(self._num_rows):
            row = []
            for j in range(self._num_cols):
                cell = self._draw_cell(i, j)
                row.append(cell)
            self._cells.append(row)


    
    def _draw_cell(self, i, j):
        x1 = self._x1 + j * self._cell_size_x
        y1 = self._y1 + i * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        # Create and draw the cell
        cell = Cell(x1, y1, x2, y2, self._win)
        cell.draw()

        # Animate
        self._animate()
        
        return cell


    
    def _animate(self):
        if self._win:
            self._win.redraw()
            time.sleep(0.05)


    def _break_entrance_and_exit(self):
        # Remove top wall of top-left cell
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw()

        # Remove bottom wall of bottom-right cell
        self._cells[self._num_rows - 1][self._num_cols - 1].has_bottom_wall = False
        self._cells[self._num_rows - 1][self._num_cols - 1].draw()

        
        if self._win:
            self._win.redraw()

    
    #wall breaking

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            directions = []

            #Check the cells that are directly adjacent to the current cell
            if i > 0 and not self._cells[i-1][j].visited:
                directions.append((-1, 0))

            if i < self._num_rows - 1 and not self._cells [i + 1][j].visited:
                directions.append((1, 0))

            if j > 0 and not self._cells[i][j-1].visited:
                directions.append((0,-1))

            if j < self._num_cols - 1 and not self._cells[i][j+1].visited:
                directions.append((0, 1))

            #not visited
            if not directions:
                self._cells[i][j].draw()
                return
            
            #random directions
            di, dj = random.choice(directions)


            #Knock down the walls between the current cell and the chosen cell.
            ni, nj = i + di, j + dj
            if di == -1:
                self._cells[i][j].has_top_wall = False
                self._cells[ni][nj].has_bottom_wall = False

            elif di == 1:  # Down
                self._cells[i][j].has_bottom_wall = False
                self._cells[ni][nj].has_top_wall = False
            elif dj == -1:  # Left
                self._cells[i][j].has_left_wall = False
                self._cells[ni][nj].has_right_wall = False
            elif dj == 1:  # Right
                self._cells[i][j].has_right_wall = False
                self._cells[ni][nj].has_left_wall = False

            # Move to the chosen cell
            self._break_walls_r(ni, nj)


    def _break_walls(self):
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def generate_maze(self):
        # Start at the top-left corner
        self._break_walls_r(0, 0)
        
        # reset the cells "visited" property
        
    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False    

    # solve the maze
    
    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()

        self._cells[i][j].visited = True

        #you are at the "end" cell (the goal)
        if i == self._num_rows-1 and j == self._num_cols-1:
            return True
        
        # Defining possible movements (di, dj): Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for di, dj in directions:
            ni, nj = i + di, j + dj

            # Checking the new cell is within bounds
            if 0 <= ni < self._num_rows and 0 <= nj < self._num_cols:
                # Checking the cell is unvisited and no wall blocks the path
                if not self._cells[ni][nj].visited:
                    if (di == -1 and not self._cells[i][j].has_top_wall) or \
                        (di == 1 and not self._cells[i][j].has_bottom_wall) or \
                        (dj == -1 and not self._cells[i][j].has_left_wall) or \
                        (dj == 1 and not self._cells[i][j].has_right_wall):

                        # Drawing a move to the new cell
                        self._cells[i][j].draw_move(self._cells[ni][nj])

                        if self._solve_r(ni, nj):
                            return True
                        
                        #Undo the move leading to a dead end
                        self._cells[i][j].draw_move(self._cells[ni][nj], undo=True)

        # If no direction works
        return False