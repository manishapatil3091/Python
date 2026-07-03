# Write a lamba function which accepts one number and returns Cube of that number

ChkCube = lambda num1 : num1*num1*num1

def main():

    no1 = int(input("Enter Number : "))
    
    CB = ChkCube(no1)  

    print("Cube is : ",CB)  
    
if(__name__ == "__main__"):
    main()