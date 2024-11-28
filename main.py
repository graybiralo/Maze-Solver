from window import Window
from drawing import Point, Line
if __name__ == "__main__":
    #create window
    win = Window(800, 600)

    #create some points
    p1 = Point(100, 100)
    p2 = Point(200, 200)
    p3 = Point(300, 100)
    p4 = Point(400, 200)

    #create line using points
    line1 = Line(p1, p2)
    line2 = Line(p3, p4)
    line3 = Line(p2, p3)

    # Draw lines on the window
    win.draw_line(line1, "red")
    win.draw_line(line2, "blue")
    win.draw_line(line3, "green")
    
    win.wait_for_close()
