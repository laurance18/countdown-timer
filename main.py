from tkinter import *

def setclockvar():
    return #TODO

def main():
    
    root = Tk()
    root.title("Countdown Timer")
    root.geometry("250x200")

    #Setting up vars
    hourvar = StringVar()
    minutevar = StringVar()
    secondvar = StringVar()
    clockvar = StringVar()

    #Setting up labels
    hourLabel = Label(root,text="Hour").grid(row=0,column=0)
    minuteLabel = Label(root,text="Minute").grid(row=0,column=1)
    secondLabel = Label(root,text="Second").grid(row=0,column=2)
    clockLabel = Label(root,text="00:00:00",font=20).grid(row=2,column=5)

    #Setting up scales
    hour = Scale(root, variable=hourvar, from_= 0, to=24).grid(row=2,column=0)
    minute = Scale(root, variable=minutevar, from_= 0, to=60).grid(row=2,column=1)
    second = Scale(root, variable=secondvar, from_= 0, to=60).grid(row=2,column=2)

    B = Button(root,text="TEST",command=lambda : print(f"{hourvar.get()}\n{minutevar.get()}\n{secondvar.get()}\n{clockvar.get()}")) 
    B.grid(row=3,column=2,columnspan = 3)

    root.mainloop()

if __name__ == "__main__":
    main()
