
import threading

def Display_Samll(str2):

    CountSmall = 0 
    for i in str2:

        if i.islower():
            CountSmall = CountSmall + 1
           
    print("Samll Character form list: ",CountSmall)
    print("Tid of Display_Samll Thread is : ",threading.get_ident())
    print("Thread Name of Display_Samll Thread is : ",threading.current_thread().name )
    print('-'*30)

def Display_Capital(str2):

    CountCapital = 0 
    for i in str2:

        if i.isupper():
            CountCapital = CountCapital + 1

    print("Capital Character form list: ",CountCapital)
    print("Tid of Display_Capital Thread is : ",threading.get_ident())
    print("Thread Name of Display_Capital Thread is : ",threading.current_thread().name)
    print('-'*30)

def Display_Digits(str2):

    CountDigit=0
    for i in str2:

        if i.isdigit():
            CountDigit = CountDigit + 1

    print("Capital Character form list: ",CountDigit)
    print("Tid of Display_Digits Thread is : ",threading.get_ident())
    print("Thread Name of Display_Digits Thread is : ",threading.current_thread().name)
    print('-'*30)

def main():

    str1 = input("Enter String : ")
    
    Samll = threading.Thread(target=Display_Samll , args=(str1,))
    Capital = threading.Thread(target=Display_Capital , args=(str1,))
    Digits = threading.Thread(target=Display_Digits , args=(str1,))

    Samll.start()
    Capital.start()
    Digits.start()

    Samll.join()
    Capital.join()
    Digits.join()

    print("Tid of Main Thread is : ",threading.get_ident())
    print("Thread Name of Display_Samll Thread is : ",threading.current_thread().name )
    print("Exit from Main Thread")

if __name__ == "__main__" :
    main()
