from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Tkinter Window")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__running = False

        # Connect the close method to the window's close button
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        # Update the GUI
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        # Main loop to keep the window open
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        # Stop the loop when the window is closed
        self.__running = False
