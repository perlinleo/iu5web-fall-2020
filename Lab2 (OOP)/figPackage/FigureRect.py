from figPackage.Color import FigureAbstractColor
from figPackage.Area import FigureAbstractArea


class Rectangle(FigureAbstractArea.FigureArea):


    FigureType = "прямоугольник"



    @classmethod
    def getFigureType(self):
        return self.FigureType

    def __init__(self, Color,Width,Height):
        self.Width, self.Height = Width,Height

        self.Color = FigureAbstractColor.FigureColor()
        self.Color.color=Color
        a=0;

    def area(self):
        return self.Width * self.Height

    def __repr__(self):
        return '\n{} {} с шириной {} и высотой {}. Площадь = {}'.format(
            self.Color.color,
            Rectangle.getFigureType(),
            self.Width,
            self.Height,
            self.area()
          )

