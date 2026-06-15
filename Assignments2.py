


# 1. write a program to diplay  value , type and memory for a variable using build in functions

import sys  #for using getsizeof


#1 Numric - Int
X1=10
print(X1)   # prints Value
print(type(X1))  # prints datatype
print(id(X1))   # prints memory address of variable

#1 Numric - Float
X2=11.23
print(X2)
print(type(X2))
print(id(X2))

#1 Numric - Complex
X3=101j
print(X3)
print(type(X3))
print(id(X3))

#2 Text - Str
name='Manisha'
print(name)
print(type(name))
print(id(name))
print(len(name))

#3 Boolean - Bool
flag=True
print(flag)
print(type(flag))
print(id(flag))
print(bin(flag))  # binary value 

#4 Sequence - List
list1=[1,2,3,4,5,6,1,2]
print(list1)
print(type(list1))
print(id(list1))

#4 Sequence - Tupple
list2=(1,2,3,4,5,6,1,2)
print(list2)
print(type(list2))
print(id(list2))
print(sys.getsizeof(list2))

#4 Sequence - Range
r=range(1,10,2)
print(r)
print(type(r))
print(id(r))
print(r[0])
print(r[1])
print(r[2])

#5 None - None
m=None
print(m)
print(type(m))
print(id(m))

#6 Mapping - dict
student = {"Name":"Manisha Patil","Age":"35","Address":"Pune"}
print(student)
print(type(student))
print(id(student))

#7 Set - set
s={10,20,30,40,50,10,20,30,60}
print(s)
print(type(s))
print(id(s))
print(len(s))

#Binary - Bytes
b=bytes([11,12,13])
print(b)
print(type(b))
print(id(b))


print('-'*70)

# 2. What is the difference between

a=10
b=10

print(id(a)) 
print(id(b)) 

a=[10]
b=[10]

print(id(a)) 
print(id(b)) 

# in 1st case values are integer which are mutable so both variable will share same memory 
#and in 2nd case it is a list and immutable so both variables will get different memory.



print('-'*70)

# 3. What does the id() function return?
#id() function returns the unique identity of an object
#Is the value returned by id() the same for two variables holding the same value?
#Not always. It depends on whether both variables point to the same object in memory.
# for eaxmple we can see above variables and what id is printed when datatype is not same for the variables




print('-'*70)

# 4 .What is the purpose of getsizeof()?
#getsizeof() is a function from Python's sys module that returns the memory size of an object in bytes.

#Why is memory size different for different data types?
# because they store data in different ways and have different internal structures




print('-'*70)

# 5. 

a=10
b=10
print(id(a)==id(b))

# the output is True because  fucntion id returns unique identity of an object and when the value for any variables are exact same the memory alloted to the varible is same , so it is returning as true




print('-'*70)

# 6. Write a program to accept 2 numbers from user and print their + - / * 

m = int
n = int

print("Enter 1st value : ")
m = int(input())

print("Enter 2nd value : ")
n = int(input())


print("Addition : ",m+n)
print("Subtraction : ",m-n)
print("Multiplication : ",m*n)
print("Division : ",m/n)




print('-'*70)

# 7. Why does the input() function always return a string? How can you convert it to another data type?

# it is designed to read input provided by user using keyboard and keyboard input is a sequence of characters so it always returns String
# to change the datatype we can use type casting function.

age = input("Enter your age: ")
print(age)
print(type(age))

age1= int(input("Enter your age: "))
print(age1)
print(type(age1))




print('-'*70)

# 8. Predit the output , explian with reason 
#i nput function will return str  because it is designed to read input provided by user using keyboard and keyboard input is a sequence of characters so it always returns String

x = input("Enter a number : ") 
print(type(x))   # prints <class 'str'>




print('-'*70)

# 9. write a program to take user's name and age and display message

name = input("Enter your Name: ")
age = int(input("Enter your Age: "))

print("Hello , you will turn ", age+1 ," next year")




print('-'*70)

# 10. What will be the output

print("10"+"20")    # prints 1020
print(10+20)    # prints 30   

#Reason : when values are given in double cotts i.e." " , it is consideres are string and will get concatinated only and when double cotts are not there the addition is done for integer value.
 