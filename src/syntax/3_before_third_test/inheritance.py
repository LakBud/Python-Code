print()
class Rectangle:
    
    """
    ? Here is a normal parent class
    
    """
    
    def __init__(self, length: float, height: float) -> None:
        self.length = length
        self.height = height
        
    def area(self) -> float:
        return self.length * self.height
    
    def show_info(self) -> None:
        print(f"Length: {self.length} | Height: {self.height} | Area: {self.area()}")


class Square(Rectangle): # ! Within the parameters, you can decide which class to inherit
    
    """
    ? A child class which represents a square, inherited from the rectangle 
    """
    
    def __init__(self, side_edge: float) -> None:
        """
        * A constructor which inherits the constructor from the Rectangle class.
        * It does this by doing the super(). method and calls the function with its own parameters.
        side_edge is the only parameter, making the height and length the same value
        """
        self.side_edge = side_edge
        super().__init__(side_edge, side_edge)
    
    def show_info(self) -> None:
        """
        Shows Info. Able to use function area() due to inheriting the Rectangle constructor 
        """
        
        print(f"Number: {self.side_edge} | Squared Number: {self.area()}")


# my_square = Square(5).show_info()
# my_rectangle = Rectangle(4, 5).show_info()


# ? You can create lists with objects, dictionarys and other elements
rectangle_list = [Rectangle(5, 4), Rectangle(2, 3), Rectangle(3, 1), Rectangle(5, 0), Rectangle(1, 4)]
square_list = [Square(5), Square(15), Square(2), Square(4), Square(9)]

for rectangle in rectangle_list:
    rectangle.show_info()
    
print("-" * 35)

for square in square_list:
    square.show_info()