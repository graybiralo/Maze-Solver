from drawing import Point, Line

class Cell:
    def __init__(self, x1, y1, x2, y2, win= None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        self._win = win 

        

    def draw(self):
        if not self._win:
            return

        # Left wall
        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "black")
        else:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "#d9d9d9")

        # Top wall
        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "black")
        else:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "#d9d9d9")

    # Right wall
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "black")
        else:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "#d9d9d9")

        # Bottom wall
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "black")
        else:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "#d9d9d9")


    def draw_move(self, to_cell, undo=False):
        # Calculate the center of the current cell
        center_x1 = (self._x1 + self._x2) // 2
        center_y1 = (self._y1 + self._y2) // 2

        # Calculate the center of the destination cell
        center_x2 = (to_cell._x1 + to_cell._x2) // 2
        center_y2 = (to_cell._y1 + to_cell._y2) // 2

        if undo:
            color = "gray"
        else:
            color = "red"

        # Draw the line
        self._win.draw_line(Line(Point(center_x1, center_y1), Point(center_x2, center_y2)), color)
