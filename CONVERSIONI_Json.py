import json

Listainseriti=[]
print("Benvenuto nel sistema Silvia. Vuoi inserire dei dati? ")
ris1=input("> ")
if(ris1=="si"):
    ris11="si"
    while ris11=="si":
        dato=input("inserisci dei dati: ")
        Listainseriti.append(dato)
        datoins=json.dumps(Listainseriti)
        ris11=input("vuoi inserire altri dati? ")
        
        
    ris4=input("Vuoi vedere i dati inseriti?")
    if(ris4=="si"):
        print(datoins)                
else:
    print("Non hai inserito alcun dato1")

Listacaricati=[]
ris2=input("Vuoi caricare i tuoi dati? ")
if(ris2=="si"):
    if(len(Listainseriti)>=0):
        for i in Listainseriti:
            datiinseriti=json.dumps(i)
            daticaricati=json.loads(datiinseriti)
            Listacaricati.append(i)
        ris3=input("Vuoi visualizzare tutti i tuoi dati caricati? ")
        if(ris3=="si"):
            print(Listacaricati)
        ris4=input("Vuoi vedere solo alcuni dati caricati? ")
        if(ris4=="si"):
            for i in range(int(len(Listacaricati))):
                print("Vuoi vedere l'elemento ",i+1,"?")
                richiesta=input("> ")
                if(richiesta=="si"):
                    print(Listacaricati[i])
                else:
                    continue
                

            # richiesta=input("inserisci l'indice rispettivo del dato che vuoi vedere: ")
            # print(Listacaricati[int(richiesta)-1])          
    else:
        print("Non hai inserito nessun dato quindi non puoi caricarli")
else:
    print("Non hai caricato nessuno dato!")

