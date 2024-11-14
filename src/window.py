from tkinter import Tk, BOTH, Canvas
from drawing_utils import Line

class Window:
    def __init__(self, width : float, height : float):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    

    def draw_line(self, line : Line, fill_color : str = "black"):
        line.draw(self.__canvas, fill_color)

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")
        
    def close(self):
        self.__running = False
    
