class Circle:

    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.1416


    def Perimeter (self):
        return 2 * self.pi * self.radius


    def Area (self):
        return self.pi * self.radius ** 2


    def Diameter (self):
        return 2 * self.radius


    def Display (self):
        print("The Perimeter is: ", (round(self.Perimeter(),2)))
        print("The Area is : ", (round(self.Area(),2)))
        print("")
        print("BONUS: The Diameter of the given radius is: ", (round(self.Diameter(),2)))


cirRad = float(input("Enter the radius of the circle: "))
circle = Circle(cirRad)
circle.Display()