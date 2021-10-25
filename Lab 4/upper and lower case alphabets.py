#  Q3. Given a string containing both upper and lower case alphabets. 
#  Write a Python program to count the number of occurrences of each alphabet (case insensitive) and display the same.

string=str(input("Enter a string: "))
string= string.upper()
res = {}
for i in string:
    if i in res:
        res[i] +=1
    else:
        res[i] = 1
print("The occurence is: "+str(res))
