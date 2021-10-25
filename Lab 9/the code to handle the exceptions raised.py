#    Q2. Assume the following Python code-
#    Rewrite the code to handle the exceptions raised. 
#    Print appropriate error messages wherever applicable.



mylist = [1,2,3,'4',5]
sum = 0
for i in mylist:
  try:
      sum += 1
   except TypeError:
       print("Invelid operand type")
   print(sum)
try:
  print(mylist[5])
except IndexError:
  print("Index out of range")

      
