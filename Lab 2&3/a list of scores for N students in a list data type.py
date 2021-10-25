#  Q2. WAP to input a list of scores for N students in a list data type. Find the score of the runner-up and print the output.
#  Sample Input
#  N = 5
#  Scores= 2 3 6 6 5
#  Sample output
#  5




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
   print("The Runner_up score is : ", second)

