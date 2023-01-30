# Importeer tkinter module. Geef naam tk.
import tkinter as tk
# Maak een lege GUI aan.
venster = tk.Tk()

# Label label aanmaken en plaatsen op GUI.
label = tk.Label(master=venster, text="De Hallo-toevoeger-2000", height=2,
                 font=("Helvetica",24))
label.grid(row=0, column=0)

# Entry veld aanmaken en plaatsen op GUI.
veld = tk.Entry(master=venster, font=("Helvetica",14) )
veld.grid(row=1, column=0)

# Functie: voegt via insert "Hallo " toe op index 0 van het Entry veld
def hallo_toevoegen():
    veld.insert(0, "Hallo ")

# Button knop aanmaken (gelinkt aan functie hallo_toevoegen)
# knop plaatsen op GUI
knop = tk.Button(master=venster, command=hallo_toevoegen, 
                 text="Voeg hallo toe!", width=50)
knop.grid(row=2, column=0, columnspan=2)

# Maak de GUI zichtbaar op de computer.
venster.mainloop()