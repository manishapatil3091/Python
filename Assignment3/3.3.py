# Predict the output and explain the reason


def fun():
    x=10
    print(x)

fun()
print(x)


# Output will be as below :

# 10
# NameError: name 'x' is not defined  - for line 9 
# reason : 1st 10 is printed because there is call to funtion fun and for line number print(x) x is not defined and it is the local variable for function fun 
