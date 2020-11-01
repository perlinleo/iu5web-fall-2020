
from abc import ABC




class FigureColor(ABC):
    """
    Абстрактный класс для цвета фигур
    """

    def __init__(self):
        self._color = None
    def colorGet(self):
        return self._color
    def colorSet(self,ColorValue):
        self._color = ColorValue
    def colorDel(self):
        del(self._color)

    color = property(colorGet,colorSet,colorDel,"Figure Color")
