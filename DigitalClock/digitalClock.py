from tkinter import *
from time import strftime

root=Tk() #creates tkinter window
root.title("Digital Computer Clock") #adds title to tkinter window

#function to display time on the label
def time():
    string=strftime("%H:%M:%S %p")
    lbl.config(text=string)
    lbl.after(1000,time)

#styling the label widget which displays the clock
lbl=Label(root,font=("arial",160,"bold"),bg="black",fg="white")
lbl.pack(anchor="center",fill="both",expand=1) #positions the label

time()
mainloop()



