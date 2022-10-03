poll_talen = ["Lucas", "Maud", "Jan", "Dillan", 
              "Piet", "Joris"]

favorite_languages = {    
    "Jan": "python",    
    "Piet": "c",    
    "Joris": "ruby"}

for naam in poll_talen:
    if naam in favorite_languages:
        print(f"bedankt voor het afnemen van de poll {naam}.")
    else:
        print(f"neem deel aan de poll {naam}.")
        x = input()
        if x == "":
            favorite_languages[naam] = x
        # else:
        #     favorite_languages.pop(naam)
print(favorite_languages)
