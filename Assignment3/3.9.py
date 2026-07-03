# What is the difference between below ? is it allowed ? why ?

x=10
x="Ten"

# 1st x refers to an integer value 10.then , x is reassigned to a string value ("Ten"). 
# Yes, it is allowed.
# This works in Python because Python is dynamically typed language and programmer need not to declare the data type of a variable.
# The type is determined automatically based on the value assigned to the variable , and so same variable can be reused for another value
# Variables are not restricted to a single data type in python 
# If nothing else refers to X variable , the memory allocated for it may later colleted by  garbage collecter.