# WAP to read an integer from STDIN. Without using any string methods, print the following on a single line.

n = int(input("Enter the Number"))
for i in range(1,n+1):
    print(i,end="")
