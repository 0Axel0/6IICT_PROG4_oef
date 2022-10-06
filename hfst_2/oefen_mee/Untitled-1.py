from tkinter import*


root = Tk()
root.geometry("500x500+0+0")

def change_cursor(event):
    if event.x in range(450, 500):
        root.config(cursor="watch")
    # else:
    #     root.config(cursor="")


root.bind("<Motion>", change_cursor)
root.mainloop()