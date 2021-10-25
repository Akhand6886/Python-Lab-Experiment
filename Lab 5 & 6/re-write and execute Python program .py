#   Q1. Using functions, re-write and execute Python program to:
#   Add natural numbers upto n where n is taken as an input from user.


n=int(input("Enter the number"))
def sum_of_number(n):
    x=0
    for i in range (1,n+1):
        x=x+i
    return x
sum_of_number(n)        
