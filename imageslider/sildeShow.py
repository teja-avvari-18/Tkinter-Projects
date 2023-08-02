from itertools import cycle #cycle returns the elements from an iterable
import tkinter as tk

class App(tk.Tk):
    def __init__(self,imageFiles,x,y,delay):
        tk.Tk.__init__(self)
        self.geometry('+{}+{}'.format(x,y))
        self.delay=delay
        self.pictures=cycle((tk.PhotoImage(file=image),image)
        for image in imageFiles)  #photoimage class is used to display images in labels,buttons etc.
        self.pictureDisplay=tk.Label(self)
        self.pictureDisplay.pack() #pack organsies widgets in blocks before placing them in the parent widget

    def showSlides(self):
        imgObject,imgName= next(self.pictures)  #next() returns the next item in an iterator
        self.pictureDisplay.config(image=imgObject)
        self.title(imgName)
        self.after(self.delay,self.showSlides)

    def run(self):
        self.mainloop()

delay=3500
imageFiles=['1.png',
            '2.png',
            '3.png']

x=100
y=50
app=App(imageFiles,x,y,delay)
app.showSlides()
app.run()




