#  Q3. Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of country stamps. Find the total number of distinct country stamps using a suitable data type. 
#  Note: Apply your knowledge of the .add() operation from set to help your friend Rupal.


n = int(input("How many country stamps do you have: "))
s = set()
for i in range(n):
    s.add(input("Enter the number of country stamp: "))
print("The total number of distinct stamps you have are: ",len(s))
