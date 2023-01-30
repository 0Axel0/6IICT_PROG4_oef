# Maak een GUI met minstens drie aparte labels:
# inhoud van labels is: Hallo, Klas en 6IICT.
import tkinter as tk
venster = tk.Tk()
label1 = tk.Label(master=venster, text="Hallo")
label2 = tk.Label(master=venster, text="klas")
label3 = tk.Label(master=venster, text="6IICT")
label1.pack()
label2.pack()
label3.pack()
venster.mainloop()