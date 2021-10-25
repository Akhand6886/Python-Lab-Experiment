#    Q3. Write a Python program to find the maximum and minimum values in a given list of tuples using lambda function.
#    Original list with tuples:
#    [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
#    Output-
#    Maximum and minimum values of the said list of tuples:
#    (74, 62)


listA=[('V',62),('VI',68),('VII',72),('VIII',70),('IX',74),('X',65)]
print("Given list:\n",listA)
result=max(listA, key=lambda i:i[1])[1]
print("Day with maximum score is:\n",result)
result=min(listA, key=lambda i:i[1])[1]
print("Day with minimum score is:\n",result)

