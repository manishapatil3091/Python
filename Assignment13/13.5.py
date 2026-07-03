# Write a progarm which accepts Marks and displays grade
#>= 75 --->Distinction
#>= 60 --->First Class
#>= 50 --->Second Class
#< 50 --->Fail

def Grade_marks(marks):

    if marks >= 75:

        return "Distinction"

    elif marks >= 60:

        return "First class"

    elif marks >= 50:

        return "Second class"

    else:

        return "Fail"

def main():

    m = int(input("Enter Marks : "))
    
    Ret = Grade_marks(m)

    print("Grade is : ",Ret)
   
if(__name__ == "__main__"):
    main()
