#   Q1. Write a Python program to:

#   1. read a ﬁle.
#   2. add backslash (\) before every double quote in the ﬁle contents.
#   3. write it to another ﬁle in the same folder.
#   4. print the contents of both the ﬁles
#   For example:
#   If the ﬁrst ﬁle is 'TestFile1.txt' with text as:
#   Jack said, "Hello Pune".
#   The output of the ﬁle 'TestFile2.txt' should be:
#   Jack said,\"Hello Pune\".


file = open(r"D:\university\Semester 2\Python Programming\Lab7and8exp.txt")
R = file.read()
print(R)
file2 = open(r"D:\university\Semester 2\Python Programming\Lab7and8exp.txt",'w')
Re = file2.write(R.replace('\" , " \\" '))
j = open("D:\university\Semester 2\Python Programming\Lab7and8exp.txt",'r')
p = j.read()
j.close()
print(p)
