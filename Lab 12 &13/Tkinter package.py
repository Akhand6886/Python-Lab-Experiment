#         Q1.
#         a)	import Tkinter package and create a window and set its title
#         b)	set the default window size using geometry function
#         c)	Create a label with “Hello” text in it and set its position on the form.
#         d)	Add a button to the window with “CLICK ME” written on it.
#         e)	change the foreground and background color for the button created above
#         f)	Create a function that will be executed when the button is clicked and print “Button was clicked” on clicking the button


def click_me():
  print("Button was clicked")

from tkinter import *
window = Tk()
window.geometry('500x400')
l = label(window,text = "Hello").pack()
button = Button(window, text= 'Click me' , bd=10,width=25, bg = "Yellow",fg = "Black",command = Click_me)
window.mainloop()
