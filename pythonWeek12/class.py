class Myshape:
    def __init__(Myshape,side, length, width, radius):
        Myshape.side = side
        Myshape.length = length
        Myshape.width = width
        Myshape.radius = radius
    
    #calculate Rectangle area (length * width)
    def Rectangle(Rectangle):
        print("Rectangle area is :" + str(Rectangle.length * Rectangle.width))
    #calculate Circle area (pi * radius * radius)
    def Circle(Circle):
        print("Circle area is :" + str(3.14 * pow(Circle.radius, 2)))
    #calculate Square area (side * side)
    def Square(Square):
        print("Square area is :" + str(Square.side * Square.side))

shape = Myshape(2, 10, 10, 2.5)
shape.Rectangle()
shape.Circle()
shape.Square()
