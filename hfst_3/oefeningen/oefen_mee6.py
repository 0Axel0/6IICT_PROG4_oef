fruit_lijst = ["Appel", "Banaan", "Kers"]

try:
    getal = input( "Geef een getal: " )
    if "." in getal:
        getal = float( getal )
    else:
        getal = int( getal )
    print( fruit_lijst[getal] )
except IndexError:
    print( "het maximum is 3" )
except ValueError:
    print("waarde moet een geheel getal zijn")
except TypeError:
    print("waarde moet een geheel getal zijn")
print("Programma klaar")  
