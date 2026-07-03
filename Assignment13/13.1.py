# Write a progarm which accepts length and width of rectangle and prints area

def Rect_area(L,W):

    area = L * W

    return area

def main():

    l = float(input("Enter length : "))

    w = float(input("Enter width : "))
    
    area = Rect_area(l,w)

    print("Area of a Rectangle is : ",area)
   
if(__name__ == "__main__"):
    main()
