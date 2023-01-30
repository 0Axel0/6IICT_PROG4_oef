# Importeer tkinter module. Geef naam tk.
import tkinter as tk

# 2 getallen vragen aan gebruiker.
getal_1 = int(input("Getal 1: "))
getal_2 = int(input("Getal 2: "))

# Maak een lege GUI aan.
venster = tk.Tk()
lijst = []

# TODO: functie aanmaken gelinkt aan Button knop.
#       Doel van functie is optellen van ingegeven getallen en plaatsen in een label.
#   
#       Niveau 2: iedere keer als de knop wordt ingeduwd, verhoogt de waarde van dit label.

def optellen():
    teller = 0
    for getal in lijst:
        teller +=1
    som = getal_1 + getal_2 + (teller*(getal_1 + getal_2))
    lijst.append(som)
    label_naam = tk.Label(master=venster, text=som, width=50, height=2)
    label_naam.pack()


# Labels aanmaken en plaatsen.
label = tk.Label(master=venster, text="Geef twee getallen in:", height=2, width=50)
label.pack()
label_1 = tk.Label(master=venster, font=("Helvetica",14), border=10, borderwidth=5, text=f"Getal 1: {getal_1}")
label_1.pack()
label_2 = tk.Label(master=venster, font=("Helvetica",14), border=10, borderwidth=5, text=f"Getal 2: {getal_2}")
label_2.pack()

# Knop voor tonen resultaat.
knop = tk.Button(master=venster, command=optellen, text="Bereken resultaat:", width=50)
knop.pack()

venster.mainloop()

# Maak de GUI zichtbaar op de computer.
venster.mainloop()