class Hond:
    def benoem(self,naam):
        self.naam = naam

    def blaf(self):
        print(f'{self.naam} zegt blaf!')
    
    def wegen(self,massa):
        self.massa = massa
        print(f"{self.naam} weegt {self.massa}kg.")

hond = Hond()
hond.benoem("Fleur")
hond.wegen(3)
hond.blaf()