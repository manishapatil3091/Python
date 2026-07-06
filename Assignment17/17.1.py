import Arithmetic as a

def main():

    no1 = int(input("Enter First number : "))
    no2 = int(input("Enter Second number : "))
    
    addn=a.Add(no1,no2)
    subn=a.Sub(no1,no2)
    multn=a.Mult(no1,no2)
    divn=a.Div(no1,no2)

    print("Addition = ",addn)
    print("Substraction = ",subn)
    print("Multiplication = ",multn)
    print("Dvision = ",divn)

if(__name__ == "__main__"):
    main()