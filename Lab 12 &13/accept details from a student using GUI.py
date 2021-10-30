#          Q3. Write a program to accept following details from a student using GUI 
#          1. Name of the student (using Textbox) 
#          2. Gender (Using radio button) 
#          3. Qualification (Using List) 
#          4. Marks of three subjects (using Textbox) 
#          Compute the percentage of the student and display it in a textbox. 


from tkinter import *
def submitt():
  name = uia.get()
  m1= marks.get()
  m2= marks.get()
  m3= marks.get()
  per = ((int(m1) + int(m2) + int(m3))/300)*100
  labe = Label(window,text = "User name is ")
