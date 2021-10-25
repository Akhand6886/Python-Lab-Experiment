#   2. Print Fibonacci series till nth term (Take input from user).


n=int(input("Enter the number:"))
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
for i in range(1, n+1):
    print(fib(i), end=" ")
