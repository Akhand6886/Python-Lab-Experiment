#   Q1. Input two values from user where the first line contains N, the number of test cases.
#   The next N lines contain the space separated values of a and b. Perform integer division and print a/b. Print the error code in the case of ZeroDivisionError or ValueError.


#   Sample input
#   1 0
#   2 $
#   3 1

#   Sample Output
#   Error Code: integer division or modulo by zero
#   Error Code: invalid literal for int() with base 10: '$'
#   3


n = int(input("No. of cases"))

for i in range(0,n):
  try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = a/b
    print(c)
   except ZeroDivisionError as e:
    print("Zero Divison Error Occured and Handled")
   except ValueError as f:
    print("Value Error occured and hanled")
   
    
