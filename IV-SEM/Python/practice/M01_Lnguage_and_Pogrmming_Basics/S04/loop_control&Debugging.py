'''
FINDING AND FIXING OF ERRORS CALLED DEBUGGING
bug is an error

TYPES OF ERRORS:
1) SYNTAX EERORS --> Missing of coion, Missing of indentation 
2) RUN-TIME ERRORS --> Any num is divisible by zero
3) LOGICAL ERRORS --> Missing of logics


DEBUGGING TECHNIQUES:

1) print() --> Run the code line by line
2) try-except--> 
3) using pdb --> Using commands we can debug
'''
'''a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = a+b
print(" value of a:" a)
print(" value of b:" b)
print(" value of c:" a+b)

try:
    a = int(input("Enter a number:"))
    print(10/a)
except ZeroDivisionError:
    print("Can not divisible by zero")
except ValueError:
    print(" invalid input.")
'''