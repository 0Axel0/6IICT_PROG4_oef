# Importeer tkinter module. Geef naam tk.
import tkinter as tk

# Vraag om de lievelingskleur van de gebruiker (rood, groen of blauw)
kleur = input("Wat is je favoriete kleur? ")

# Maak een lege GUI aan.
venster = tk.Tk()

label = tk.Label(master=venster, text="wat is je favoriete kleur?", height=2)
label.grid(row=0, column=0, columnspan=2)

# TODO: vertaal input van gebruiker naar het Engels
if kleur == "rood":
    color = "red"
if kleur == "blauw":
    color = "blue"
if kleur == "groen":
    color = "green"

# TODO: maak functie aan die het label in de ingegeven kleur laat zien.
def colortext():
    tekst = f"mijn favoriete kleur is {kleur}."
    label_naam = tk.Label(master=venster, text=tekst, width=50, height=2,fg=color)
    label_naam.grid(row=2, column=0, columnspan=2)

knop = tk.Button(master=venster, text="Klik op mij!", command=colortext)
knop.grid()

# Maak de GUI zichtbaar op de computer.
venster.mainloop()