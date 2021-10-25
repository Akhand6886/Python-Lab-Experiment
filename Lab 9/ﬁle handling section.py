#   Q3. You have already created a Python program to implement the following in ﬁle handling section: 
#   1. read a ﬁle.
#   2. add backslash (\) before every double quote in the ﬁle contents.
#   3. write it to another ﬁle in the same folder.
#   4. print the contents of both the ﬁles.
#   For example:
#   If the ﬁrst ﬁle is 'TestFile1.txt' with text as:
#   Jack said, "Hello Pune".
#   The output of the ﬁle 'TestFile2.txt' should be:
#   Jack said,\"Hello Pune\".
#   Modify your code to implement Exception handling. 
#   Print appropriate error messages wherever applicable.


try:
   file = open('Test file1.txt','r')
   file2 = open('Test file2.txt')
   data file.read()
   file2.write(data.replace()) 
   data = file.close() 
