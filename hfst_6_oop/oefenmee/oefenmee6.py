class Hond:
    def __init__(self,naam,massa):
        self.naam = naam
        self.massa = massa
        print(f"{self.naam} weegt {self.massa}kg.")


hond = Hond("Floris",8)
hond2 = Hond("Fido",3)