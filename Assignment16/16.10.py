def ChkLen(name1):
    
    return len(name1)
    
def main():

    name = input("Enter a Name : ")
    result = ChkLen(name)

    print("Length is : ", result)
    
if(__name__ == "__main__"):
    main()