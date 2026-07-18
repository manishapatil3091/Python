class Arithmatic:
    # Constructor
    def __init__(self):

        #Instance Variables as in init method
        self.Value1 = 0
        self.Value2 = 0

     #Instance Method
    def Accept(self):
        self.Value1 = int(input("Enter Value1 : "))
        self.Value2 = int(input("Enter Value2 : "))


    def Addition(self):
        self.add = self.Value1 + self.Value2
        print("Addition is : ",self.add)

    def Substraction(self):
        self.sub = self.Value1 - self.Value2
        print("Substraction is : ",self.sub)

    def Multiplication(self):
        self.mult = self.Value1 * self.Value2
        print("Multiplication is : ",self.mult)

    def Division(self):
        self.div = self.Value1 / self.Value2
        print("Division is : ",self.div)

def main():
    Obj1 = Arithmatic()
    
    Obj1.Accept()
    Obj1.Addition()
    Obj1.Substraction()
    Obj1.Multiplication()
    Obj1.Division()

if __name__ == "__main__":
    main()
