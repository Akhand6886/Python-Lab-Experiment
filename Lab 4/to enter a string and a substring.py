#  Q1. .  WAP to enter a string and a substring. 
#  You have to print the number of times that the substring occurs in the given string. 
#  String traversal will take place from left to right, not from right to left.


string= str(input("Enter a string: "))
sub_str= str(input("Enter a subsrtring: "))
print("The string is: ",string)
print("The subsrtring is: ", sub_str)
a=len(string)
b=len(sub_str)
res=0;
for i in range (a-b+1):
    j=0;
    while j<b:
        if (string[i+j] != sub_str[j]):
            break
        j+=1
    if(j==b):
        res+=1
        j=0
print("The no. of times subsrtring occurs is: ",res)
