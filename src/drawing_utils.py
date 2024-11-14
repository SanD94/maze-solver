from tkinter import Canvas


# for pixels
# x = 0 left
# y = 0 top
class Point:
    def __init__(self, x : float, y : float):
        self.__x = x
        self.__y = y

    def __iter__(self):
        for val in self.__dict__.values():
            yield val
    
class Line:
    def __init__(self, p0 : Point, p1 : Point):
        self.__p0 = p0
        self.__p1 = p1
    
    def draw(self, canvas : Canvas, fill_color : str):
        canvas.create_line(*self.__p0, *self.__p1, fill=fill_color, width=2)