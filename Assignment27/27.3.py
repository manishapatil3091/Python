class Numbers:

    def __init__(self,value ):

        self.Value = value
        
    def ChkPrime(self):

        if self.Value >= 1:
            for i in range (2,self.Value):
                if(self.Value % i) == 0:
                    return False
            return True
        
    def ChkPerfect(self):

        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i

        return total == self.Value
        
    def Factors(self):
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        
        
    def SumFactors(self):
        total = 0

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                total += i

        return total
        
def main():

    Val = int(input("Enter Value : "))

    Obj1 = Numbers(Val)
    
    print("Prime :", Obj1.ChkPrime())
    print("Perfect :", Obj1.ChkPerfect())
    print("Factors : " )
    Obj1.Factors()
    print()
    print("Sum of Factors :",Obj1.SumFactors())
    
   
if __name__ == "__main__":
    main()
