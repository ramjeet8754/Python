
# Import the tkinter module
from tkinter import *

# Create the root window
root = Tk()

# Set the title of the root window
root.title("Welcome to Aabhira Lecture's")

# Set the geometry (width x height)
root.geometry('400x350')

#root.title("Students")
#root.geometry("250x300")

#creating button and text login
button1=Button(root,text="Login")

#creating pack or grid to left side
button1.pack(side=LEFT)

button2=Button(root,text="Sumbit")
button2.pack(side=RIGHT)

#Here creating label and place 
L1=Label(root,text="Name")
L1.place(x=50,y=50)

e1=Entry(root)
e1.place(x=100,y=50)

L2=Label(root,text="Password")
L2.place(x=50,y=100)

e2=Entry(root)  
e2.place(x=105,y=105)


#n=Label(root,text="name")
#n.grid(row=0,column=0)


# Execute the Tkinter event loop
root.mainloop() 

