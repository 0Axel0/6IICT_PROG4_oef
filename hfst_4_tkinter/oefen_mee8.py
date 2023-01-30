# importeer tkinter
import tkinter as tk
# maak een nieuw venster aan
venster = tk.Tk()
# maak een nieuwe label aan
label = tk.Label(master=venster, text="Welke website wil je bezoeken?", height=2)
label.grid(row=0, column=0, columnspan=2)
# maak een invulbare balk aan
link_1 = tk.Entry(master=venster, width=33, font=("Helvetica",14),
                  border=10, borderwidth=5)
link_1.grid(row=1, column=0)
# maak een 2de invulbare balk aan
link_2 = tk.Entry(master=venster, width=33, font=("Helvetica",14), 
                  border=10, borderwidth=5)
link_2.grid(row=1, column=1)
# maak de functie aan die de tekst gaat verwijderen
def reset_links():
    link_1.delete(0, 1)

    web_2 = link_2.get()
    link_2.delete( 0, web_2.find(".")+1 )
# maak een knop aan die de delete functie activeert
knop = tk.Button(master=venster, command=reset_links, 
                 text="Reset input!", width=50)
knop.grid(row=2, column=0, columnspan=2)
# run het programma
venster.mainloop()