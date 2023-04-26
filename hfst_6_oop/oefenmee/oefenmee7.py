class Hond:
    def __init__(self,naam,massa):
        self.naam = naam
        self.massa = massa
        print(f"{self.naam} weegt {self.massa}kg.")
    
    def wijzig_naam(self,nieuwe_naam):
        print(f"{self.naam} heet nu {nieuwe_naam}.")
        self.naam = nieuwe_naam
    
    def eten(self,hoeveelheid):
        self.massa = self.massa + (hoeveelheid*0.3)
        print(f"{self.naam} heeft gegeten en weegt nu {round(self.massa,2)}kg.")

hond = Hond("Lucky",5)
hond.wijzig_naam("Bolly")
hond.eten(0.5)
hond.eten(0.7)
hond.eten(0.3)

hond2 = Hond("hond",9)
# hond2.wijzig_naam("Mercie")
hond2.eten(0.5)
hond2.eten(0.5)
hond2.eten(0.5)