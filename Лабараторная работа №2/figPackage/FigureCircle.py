
from figPackage.Color import FigureAbstractColor
from figPackage.Area import FigureAbstractArea

from math import pi

class Circle(FigureAbstractArea.FigureArea):


    FigureType = "круг"
    
    
    @classmethod
    def getFigureType(self):
        return self.FigureType

    def __init__(self, Color,Radius):
        self.Radius = Radius
        self.Color = FigureAbstractColor.FigureColor()
        self.Color.color=Color

    def area(self):
        return pi*(self.Radius**2)

    def __repr__(self):
        return '\n{} {} с радиусом {}. Площадь = {}'.format(
            self.Color.color,
            Circle.getFigureType(),
            self.Radius,
            self.area()
          )

