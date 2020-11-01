from figPackage.FigureRect import Rectangle
from figPackage.FigureCircle import Circle
from figPackage.FigureSquare import Square




def main():
        
    square = Square("Черный",10)

    rect = Rectangle("Желтый", 10,10)

    circle = Circle("Белый", 4)

    print(rect,circle,square)

if __name__ == '__main__':
    main()


