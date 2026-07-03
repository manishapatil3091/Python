#  Write a progarm which accepts two numbers and prints addition , substraction , multiplication and division

def Calc(num1,num2):

    ad = num1 + num2
    sub = num1 - num2
    mult = num1 * num2
    div = num1 / num2

    return  ad , sub , mult , div 

def main():

    no1 = int(input("Enter First Number : "))
    no2 = int(input("Enter Second Number : "))
    
    ad,sub,mult,div = Calc(no1,no2)

    print("Addition : ", ad )
    print("Substraction : ", sub )
    print("Multiplication : ", mult )
    print("Division : ", div )
   
if(__name__ == "__main__"):
    main()