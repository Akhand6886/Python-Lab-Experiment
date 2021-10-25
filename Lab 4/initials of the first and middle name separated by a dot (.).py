#   Q2. WAP to input the first name, middle and last name of a person. 
#   Your task is to print the initials of the first and middle name separated by a dot (.)
#   The last name should be followed by a dot and a space where the first letter is capital


name = str(input("Enter a string: "))

l=name.split()
n= ""
for i in range (len(l)-1):
    s=l[i]
    n += (s[0].upper()+'.') 
n += l[-1].title() 
print("The titled name is: ",n)
