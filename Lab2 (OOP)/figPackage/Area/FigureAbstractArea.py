from abc import ABC




class FigureArea(ABC):
    """
    Абстрактный класс для всех площади фигур
    """
    def area(self):
         pass
        #будет переписана при наследовании для каждой фигуры по-своему
       