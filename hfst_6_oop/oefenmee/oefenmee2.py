class Hond:
    naam = 'mercie'
    massa = 5
    def blaf(self):
        print(f'{self.naam} zegt blaf!')
    def weegschaal(zichzelf):
        print(f'{zichzelf.naam} weegt {zichzelf.massa}Kg')

hond = Hond()
huisdier = Hond()

print(hond.naam)
print(hond.massa)
print(type(hond))

print(huisdier.massa)
print(huisdier.naam)
print(type(huisdier))

hond.blaf()
hond.weegschaal()