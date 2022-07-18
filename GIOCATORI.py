Giocatori={"Buddy":"Alzatore", "Jack":"Libero","Barbalbero":"Centrale","Platano-Picchiatore":"Centrale", "Fierobecco":"Laterale","Picklet":"Laterale", "Ray":"Opposto" }
print(Giocatori)
print("------------------------AGGIORNAMENTO RUOLO GIOCATORI------------------------")
for i in Giocatori:
    print(i, Giocatori[i])
    z=input("Vuoi cambiargli ruolo? Sì o No ")
    if(z.lower().replace()=="sì" or z.lower().replace()=="si"):
        v=input("Ma ne sei sicuro? Sì o No ")
        if(v.lower.replace()=="sì" or z.lower().replace() == "si"):
            ruolo=input("che ruolo deve avere? ")
            Giocatori.update({i:ruolo.capitalize()})
        elif(v.lower().replace() =="no"):
            continue
        else:
            print("ATTENZIONE: scegli tra le opzioni indicate!")
            i=i-1
    elif(z.lower().replace()=="no"):
        continue
    else:
        print("ATTENZIONE: scegli tra le opzioni indicate!")
        i=i-1

print(Giocatori) 