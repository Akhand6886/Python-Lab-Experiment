#   Q2. Consider a ﬁle 'rhyme.txt' in D Drive with following text:

 
#   Write a Python program to count the words in the ﬁle using a dictionary (use space as a delimiter). 
#   Find unique words and the count of their occurrences (ignoring case). Write the output in another ﬁle "words.txt" at the same location


file = open(r"D:\university\Semester 2\Python Programming\Lab7and8exp.txt")
data = file.read()
occurences = data.count("jingle")
print("Number of Ocurrence of the word int the file :",occurences)

