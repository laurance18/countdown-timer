from tkinter import *
from datetime import datetime

def modifyclockvar(h,m,s):
    #Formatting clockvar strings
    if int(h.get())<10:
        h = f"0{h.get()}"
    else:
        h = f"{h.get()}"
    if int(m.get())<10:
        m = f"0{m.get()}"
    else:
        m = f"{m.get()}"
    if int(s.get())<10:
        s = f"0{s.get()}"
    else:
        s = f"{s.get()}"


    clock = f"{h}:{m}:{s}"
    clockvar.set(clock)

def main():
    #Mainwindow
    root = Tk()
    root.title("Countdown Timer")
    root.geometry("250x200")

    #Setting up vars
    hourvar = StringVar()
    minutevar = StringVar()
    secondvar = StringVar()
    
    global clockvar
    clockvar = StringVar()
    clockvar.set("00:00:00")

    #Setting up labels
    hourLabel = Label(root,text="Hour").grid(row=0,column=0)
    minuteLabel = Label(root,text="Minute").grid(row=0,column=1)
    secondLabel = Label(root,text="Second").grid(row=0,column=2)
    clockLabel = Label(root,textvariable=clockvar,font=20).grid(row=2,column=5)

    #Setting up scales
    hour = Scale(root, variable=hourvar, from_= 0, to=24).grid(row=2,column=0)
    minute = Scale(root, variable=minutevar, from_= 0, to=60).grid(row=2,column=1)
    second = Scale(root, variable=secondvar, from_= 0, to=60).grid(row=2,column=2)

    B = Button(root,text="START TIMER",command=lambda : modifyclockvar(hourvar,minutevar,secondvar))
    B.grid(row=3,column=0,columnspan = 3) 

    root.mainloop()

if __name__ == "__main__":
    main()
