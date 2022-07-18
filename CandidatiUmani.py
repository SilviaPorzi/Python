print("------------------------------Inserimento candidati(umani)------------------------------")
Listacandidati=dict()
i=0
while i>=0: 
    i=i+1
    print("Sei un umano o un robot?")
    x=input("> ")
    if(x.lower().replace() =="umano"):
        nome=input("Scrivi il tuo nome: ")
        cognome=input("Scrivi il tuo cognome: ")
        Listacandidati.update({i:nome +" "+ cognome})
        y=input("Sei l'ultimo candidato? sì o no --> ")
        if(y.lower().replace()=="sì" or y.lower().replace() =="si"):
            break
        elif(y.lower().replace()=="no"):
            continue
        else:
            print("ATTENZIONE: scegli tra le opzioni indicate!")
            i=i-1
    elif(x.lower().replace() =="robot"):
        print("Mi dispiace, si accettano solo candidati umani")
        i=i-1
    else:
        print("ATTENZIONE: scegli tra le opzioni indicate!")
        i=i-1
print(Listacandidati)