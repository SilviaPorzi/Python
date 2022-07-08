class lista():
    Lista1=[ ]
    nome= "nome"
    cognome = "cognome"
    età = 1
    professione = "professione"

Dati=lista()

Dati.nome = input("inserisci il tuo nome")
if(type(Dati.nome) == str):
    Dati.Lista1.append(Dati.nome)

Dati.cognome =input("inserisci il tuo cognome")
if(type(Dati.cognome)==str):
    Dati.Lista1.append(Dati.cognome)

Dati.età =input("scrivi la tua età")
if(int(Dati.età) ):
    Dati.Lista1.append(Dati.età)

Dati.professione =input("scrivi la tua professione")
if(type(Dati.professione)==str):
    Dati.Lista1.append(Dati.professione)


print(Dati.Lista1)


