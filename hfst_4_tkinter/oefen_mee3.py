# Importeer tkinter module. Geef naam tk.
import tkinter as tk

# Maak een lege GUI aan.
venster = tk.Tk()

# TODO: maak de afbeelding van oefen mee 3.
label_1 = tk.Label(master=venster, text="Hallo")
label_4 = tk.Label(master=venster, text= "klas")
label_6 = tk.Label(master=venster, text= "6IICT!")

label_1.grid(row=0, column=0)
label_4.grid(row=0, column=1)
label_6.grid(row=1, column=1)

# Maak de GUI zichtbaar op de computer.
venster.mainloop()