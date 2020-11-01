
from figPackage.FigureRect import Rectangle


class Square(Rectangle):


    FigureType = "квадрат"
    
    @classmethod
    def getFigureType(self):
        return self.FigureType

    def __init__(self, Color,Side):
        self.Side = Side
        super().__init__(Color,Side,Side)
    def area(self):
        return self.Side**2

    def __repr__(self):
        return '\n{} {} со стороной {}. Площадь = {}'.format(
            self.Color.color,
            Square.getFigureType(),
            self.Side,
            self.area()
          )


