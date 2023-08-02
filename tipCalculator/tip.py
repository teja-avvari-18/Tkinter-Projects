from tkinter import Tk,Radiobutton,Button,Label,StringVar,IntVar,Entry

class TipCalculator():
    def __init__(self):
        window=Tk() #creates a application window
        window.title("Tip Calculator App")
        window.configure(background="sky blue") #set background color to sky blue
        window.geometry("400x400") #define size of the window
        window.resizable(width=False,height=False) #we cannot resize the window size
        self.mealCost=StringVar()
        self.tipPercent=IntVar()
        self.tip=StringVar()
        self.totalCost=StringVar()

        tipPercents=Label(window,text="Tip Percentages",bg="orange",fg="white")
        tipPercents.grid(column=0,row=0,padx=15)

        billAmount=Label(window,text="Bill Amount",bg="Black",fg="white")
        billAmount.grid(column=1,row=0,padx=15)

        billAmountEntry=Entry(window,textvariable=self.mealCost,width=14)
        billAmountEntry.grid(column=2,row=0)


        fivePercentTip=Radiobutton(window,text="5%",variable=self.tipPercent,value=5)
        fivePercentTip.grid(column=0,row=1)

        tenPercentTip = Radiobutton(window, text="10%", variable=self.tipPercent, value=10)
        tenPercentTip.grid(column=0, row=2)

        fifteenPercentTip = Radiobutton(window, text="15%", variable=self.tipPercent, value=15)
        fifteenPercentTip.grid(column=0, row=3)

        twentyPercentTip = Radiobutton(window, text="20%", variable=self.tipPercent, value=20)
        twentyPercentTip.grid(column=0, row=4)

        twentyFivePercentTip = Radiobutton(window, text="25%", variable=self.tipPercent, value=25)
        twentyFivePercentTip.grid(column=0, row=5)

        thirtyPercentTip = Radiobutton(window, text="30%", variable=self.tipPercent, value=30)
        thirtyPercentTip.grid(column=0, row=6)


        tipAmountLabel=Label(window,text="Tip Amount",bg="red",fg="white")
        tipAmountLabel.grid(column=1,row=3,padx=15)
        tipAmountEntry=Entry(window,textvariable=self.tip,width=14)
        tipAmountEntry.grid(column=2,row=3)

        billTotalLbl=Label(window,text="Bill Total",bg="red",fg="white")
        billTotalLbl.grid(row=5,column=1,padx=15)
        billTotalEntry=Entry(window,textvariable=self.totalCost,width=14)
        billTotalEntry.grid(column=2,row=5)

        calculateBtn=Button(window,text="Calculate",bg="green",fg="white",command=self.calculate)
        calculateBtn.grid(column=1,row=7,padx=15)

        clearBtn=Button(window,text="Clear",bg="Black",fg="white",command=self.clear)
        clearBtn.grid(column=2,row=7)

        window.mainloop()

    def calculate(self):
        preTip=float(self.mealCost.get())
        percentage=self.tipPercent.get()/100
        tipAmountEntry=preTip*percentage
        self.tip.set(tipAmountEntry)

        finalBill=preTip+tipAmountEntry
        self.totalCost.set(finalBill)

    def clear(self):
        self.totalCost.set("")
        self.mealCost.set("")
        self.tip.set("")








TipCalculator()

