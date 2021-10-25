# Q1. WAP to read the record of n students in a dictionary containing key/value pairs of name: [marks]. Print the average of the marks obtained by the particular student correct to 2 decimal places


#  Input Format
#  The first line contains the integer n, the number of student’s records. The next n lines contain the names and marks obtained by a student, each value separated by a space. 
#  Sample Input
#  3
#  Krishna 67 68 69
#  Arjun 70 98 63
#  Malika 52 56 60
#  Sample Output 
#  56.00
 
NumList = []
Number = int(input("How many students you want to enter:  "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d student : " %i))
    NumList.append(value)
first = second = NumList[0]
for j in range(1, Number):
    if(NumList[j] > first):
        second = first
        first = NumList[j]
    elif(NumList[j] > second and NumList[j] < first):
        second = NumList[j]
  print("The Runner_up is : ", second)
