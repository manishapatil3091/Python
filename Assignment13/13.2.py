# Write a progarm which accepts redius of circle and prints area of circle

def Cir_area(R):

    area = 3.14 * R * R

    return area

def main():

    r = float(input("Enter Redius : "))
    
    area = Cir_area(r)

    print("Area of a Circle is : ",area)
   
if(__name__ == "__main__"):
    main()
