# importeer tkinter
import tkinter as tk
# maak een nieuw venster aan
venster = tk.Tk()
# maak een nieuwe label aan die vraagt naar de naam van de gebruiker
label = tk.Label(master=venster, text="Geef naam op: ", width=15, height=2, 
                 highlightthickness=2, highlightbackground="black")
label.grid(row=0, column=0)
# zorg dat de gebruiker zijn/haar naam kan invoeren
veld = tk.Entry(master=venster, width=50, fg="red")
veld.grid(row=0, column=1)
# de functie die de tekst met de naam van de gebruiker print
def display_naam():
    tekst = f"Hallo, mijn naam is {veld.get()}!"
    label_naam = tk.Label(master=venster, text=tekst, width=50, height=2)
    label_naam.grid(row=2, column=0, columnspan=2)
# de knop dat de gebruiker zijn/haar naam kan invoeren in het systeem
knop = tk.Button(master=venster, command=display_naam, text="Voer in!", width=50)
knop.grid(row=1, column=0, columnspan=2)
# run het programma
venster.mainloop()
