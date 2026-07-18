class Circle:
    # Class Variable as those are out of init method
    PI = 3.14

    # Constructor
    def __init__(self):

        #Instance Variables as in init method
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

     #Instance Method
    def Accept(self):
        self.Radius = float(input("Enter Radius: "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius :  ", self.Radius)
        print("Area : ", self.Area)
        print("Circumference :  ", self.Circumference)

def main():
    Obj1 = Circle()
    
    Obj1.Accept()
    Obj1.CalculateArea()
    Obj1.CalculateCircumference()
    Obj1.Display()

if __name__ == "__main__":
    main()
