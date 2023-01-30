import tkinter as tk

venster = tk.Tk()

settings = {
    "master": venster,
    "padx": 120,
    "pady": 20,
    "highlightthickness": 2,
    "highlightbackground": "black"
}

getal = []
teken1 = 0

def label1():
    getal.append(1)
    label_x = tk.Label(master=venster, text=getal, width=50, height=2)
    label_x.grid(row = 0, column = 4)
def label2():
    getal.append(2)
    label_x = tk.Label(master=venster, text=getal, width=50, height=2)
    label_x.grid(row = 0, column = 4)
def label3():
    getal.append(3)
    label_x = tk.Label(master=venster, text=getal, width=50, height=2)
    label_x.grid(row = 0, column = 4)
def label4():
    getal.append(4)
    label_x = tk.Label(master=venster, text=getal, width=50, height=2)
    label_x.grid(row = 0, column = 4)
def label5():
    getal.append(5)
    label_x = tk.Label(master=venster, text=getal, width=50, height=2)
    label_x.grid(row = 0, column = 4)
def label6():
    getal.append(6)
    label_x = tk.Label(master=venster, text=getal, width=50, height=2)
    label_x.grid(row = 0, column = 4)
def label7():
    getal.append(7)
    label_x = tk.Label(master=venster, text=getal, width=50, height=2)
    label_x.grid(row = 0, column = 4)
def label8():
    getal.append(8)
    label_x = tk.Label(master=venster, text=getal, width=50, height=2)
    label_x.grid(row = 0, column = 4)
def label9():
    getal.append(9)
    label_x = tk.Label(master=venster, text=getal, width=50, height=2)
    label_x.grid(row = 0, column = 4)
def label0():
    getal.append(0)
    label_x = tk.Label(master=venster, text=getal, width=50, height=2)
    label_x.grid(row = 0, column = 4)
def labelmin():
    getal1 = getal
    if teken1 != "+":
        teken1 = "-"
    else:
        teken2 = "-"
    print(getal1)
    label_x = tk.Label(master=venster, text=getal1, width=50, height=2)
    label_x.grid(row = 0, column = 4)
    getal.clear()
def labelplus():
    global teken1
    if teken1 != "-":
        teken1 = "+"
    else:
        teken2 = "+"
    getal2 = getal
    print(getal2)
    label_x = tk.Label(master=venster, text=getal, width=50, height=2)
    label_x.grid(row = 0, column = 4)
    getal.clear()
def labelclr():
    getal.clear()
    label_x = tk.Label(master=venster, text="", width=50, height=2)
    label_x.grid(row = 0, column = 4)
def labelenter():
    if teken1 == "+":
        uitkomst = getal1 + getal2
    else:
        uitkomst = getal1 - getal2
    label_x = tk.Label(master=venster, text=uitkomst, width=50, height=2)
    label_x.grid(row = 0, column = 4)



knop_1 = tk.Button(width= 10, height= 5, master=venster, text="1", command=label1)
knop_1.grid(row=0,column=0)
knop_2 = tk.Button(width= 10, height= 5, master=venster, text="2", command=label2)
knop_2.grid(row=0,column=1)
knop_3 = tk.Button(width= 10, height= 5, master=venster, text="3", command=label3)
knop_3.grid(row=0, column=2)
knop_4 = tk.Button(width= 10, height= 5, master=venster, text="4", command=label4)
knop_4.grid(row=1, column=0)
knop_5 = tk.Button(width= 10, height= 5, master=venster, text="5", command=label5)
knop_5.grid(row=1, column=1)
knop_6 = tk.Button(width= 10, height= 5, master=venster, text="6", command=label6)
knop_6.grid(row=1, column=2)
knop_7 = tk.Button(width= 10, height= 5, master=venster, text="7", command=label7)
knop_7.grid(row=2, column=0)
knop_8 = tk.Button(width= 10, height= 5, master=venster, text="8", command=label8)
knop_8.grid(row=2, column=1)
knop_9 = tk.Button(width= 10, height= 5, master=venster, text="9", command=label9)
knop_9.grid(row=2, column=2)
knop_10 = tk.Button(width= 10, height= 5, master=venster, text="0", command=label0)
knop_10.grid(row=3, column=0)
knop_11 = tk.Button(width= 10, height= 5, master=venster, text="-", command=labelmin)
knop_11.grid(row=3, column=1)
knop_12 = tk.Button(width= 10, height= 5, master=venster, text="+", command=labelplus)
knop_12.grid(row=3, column=2)
knop_13 = tk.Button(width= 10, height= 5, master=venster, text="clr", command=labelenter)
knop_13.grid(row=4, column=0,columnspan=1)
knop_14 = tk.Button(width= 10, height= 5, master=venster, text="enter", command=labelenter)
knop_14.grid(row=4, column=1,columnspan=1)

scherm = tk.Label(master=venster, text="", width=50, height=2)
scherm.grid(row = 1, column = 3)

venster.mainloop()