class Demo:
    # Class Variable as those are out of init method
    Value = 10 

    # Constructor
    def __init__(self, no1 , no2 ):

        #Instance Variables as in init method
        self.No1 = no1
        self.No2 = no2

     #Instance Method
    def fun(self):
        
        print("Inside Instance Method named Fun")
        print(self.No1)
        print(self.No2)

    def gun(self):
        
        print("Inside Instance Method named Gun")
        print(self.No1)
        print(self.No2)

def main():
    Obj1 = Demo(11,21)
    Obj2 = Demo(51,101)

    Obj1.fun()
    Obj2.fun()
    Obj1.gun()
    Obj2.gun()

if __name__ == "__main__":
    main()
