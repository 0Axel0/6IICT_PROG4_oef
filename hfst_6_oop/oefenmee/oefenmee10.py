import random

class Hond:
    positie = ["living", "keuken", "garage", "gang", "tuin"]
    def __init__(self,naam):
        self.naam = naam
        self.positie = random.choice(self.positie)

    def ziet_hond(self, andere_hond):
        if self.positie == andere_hond.positie:
            print(f"{self.naam} ziet {andere_hond.naam} in {self.positie}")

            gekozen = random.choice([self,andere_hond])
            gekozen.positie = random.choice(self.positie)
            print(f"{gekozen.naam} is bang en rent naar de {self.positie}.")
        else:
            print(f"{self.naam} ziet geen hond in de {self.positie}.")

hond_1 = Hond("Lulu")
hond_2 = Hond("Floris")
hond_3 = Hond("Ranger")

hond_1.ziet_hond(hond_2)
hond_1.ziet_hond(hond_3)
hond_2.ziet_hond(hond_3)