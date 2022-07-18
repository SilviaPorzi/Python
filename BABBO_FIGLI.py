class Babbo:

    def __init__(self, n1):
        self.cognomebabbo=n1  

    def Creafigli(self, Listanomi):
        figlio=dict()
        for i in Listanomi:
            elemento=Figlio(self.cognomebabbo, i)
            figlio.update({elemento.nome:elemento.cognomebabbo})
        return print(figlio)

class Figlio(Babbo):
    def __init__(self, n1, n2):
        self.nome=n2
        Babbo.__init__(self, n1)


#creo la lista coi nomi dei figli:
Lista=[]
print("--------INSERIMENTO FIGLI--------")
ris=input("Hai figli? \n (rispondi solo sì o no) -> ")
if(ris.lower().replace()=="sì" or ris.lower().replace()=="si"):
    while(ris.lower().replace()=="sì" or ris.lower().replace()=="si"):
        nomefiglio=input("Inserisci il nome di tuo/a figlio/a: ")
        Lista.append(nomefiglio.capitalize())
        ris1=input("Hai altri/ figli/e? \n (rispondi solo sì o no) -> ")
        if(ris1.lower().replace()=="sì" or ris1.lower().replace()=="si"):
            while(ris1.lower().replace()=="sì" or ris1.lower().replace()=="si"):
                nomefiglio=input("Inserisci il nome di tuo/a figlio/a: ")
                Lista.append(nomefiglio.capitalize())
                ris1=input("Hai altri figli? \n (rispondi solo sì o no) -> ")
            else:
                if(ris1.lower().replace()=="no"):
                    print(Lista)
                    break
        elif(ris1.lower().replace()=="no"):
            print(Lista)
            break
elif(ris.lower().replace()=="no"):
    print(Lista)

#creo il cognome del babbo e successivamente una lsita con i cognomi e nomi dei suoi figli:
cognomebab=input("Inserisci il cognome del babbo: ")
b=Babbo(cognomebab.capitalize())
x=b.Creafigli(Lista)