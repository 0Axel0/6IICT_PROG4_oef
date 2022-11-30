""" Niveau 1 """
try:
    num_lijst = [ 100, 101, 0, "103", 104 ]
    index = int( input( "Geef een index: " ) )
    print(num_lijst[index])
except ValueError:
    print("index moet een geheel getal zijn")
except TypeError:
    print("index moet een geheel getal zijn")
except IndexError:
    print("maximum is 5")
except ZeroDivisionError:
    print("getal niet deelbaar door 0")
else:
    try:
# """ Niveau 2 (haal uit commentaar) """
        print( f"100 / {num_lijst[index]} = {100/num_lijst[index]}" ) 
    except ValueError:
        print("index moet een geheel getal zijn")
    except TypeError:
        print("index moet een geheel getal zijn")
    except IndexError:
        print("maximum is 5")
    except ZeroDivisionError:
        print("getal niet deelbaar door 0")
    finally:
        print( "Geldig getal als index opgegeven." )