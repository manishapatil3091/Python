

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
