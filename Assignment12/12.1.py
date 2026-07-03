# Write a progarm which accepts one character and checks whether it is vowel or consonant

def Check_vowel(ch):

    if ch == "A" or ch == "E" or ch == "I" or ch == "O" or ch == "U" or ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":

        return True

    else:

        return False

def main():

    a = input("Enter a Character : ")
    
    ret = Check_vowel(a)

    if ret == True:

        print("It is a Vowel")

    else:

        print("It is a Consonant")
   
if(__name__ == "__main__"):
    main()

