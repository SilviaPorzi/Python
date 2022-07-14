
class Animale:
    def __init__(self,n1):
        self.nome=n1

    def creaFelino(self, vel):
        self = Felino(self.nome, vel)
        return self

    def creaCanide(self, raz):
        self = Canide(self.nome, raz)
        return self

    def creaUccello(self, uova):
        self = Uccello(self.nome, uova)
        return self


class Felino(Animale):
    def __init__(self, n1, v1):
        self.velocita=v1
        super().__init__(n1)

    def stampa(self):
        print("Il felino è un/uno/una ", self.nome, " che può raggiungere la velocità di ", self.velocita)

class Canide(Animale):
    def __init__(self, n1, r1):
        self.razza=r1
        super().__init__(n1)

    def stampa(self):
        print("Il cane si chiama ", self.nome," ed è di razza ", self.razza)

class Uccello(Animale):
    def __init__(self, n1, c1):
        self.coloreuova=c1
        super().__init__(n1)

    def stampa(self):
        print("L'uccello è un/uno/una ", self.nome," che fa le uova di colore ", self.coloreuova)    

while True:
    print("SCEGLI IL TIPO DI ANIMALE TRA I SEGUENTI \n 1. FELINO \n 2. CANIDE \n 3. UCCELLO \n 4. NESSUNO DEI TRE")
    x=input("> ")
    if(x == "1"):
        nome=input("inserisci il tipo di felino: ")
        attr=input("inserisci la velocità massima che può raggiungere: ")
        anima=Animale(nome)
        felino=anima.creaFelino(attr)
        felino.stampa()
        # Lista_felini.append(felino)
    elif(x == "2"):
        nome=input("inserisci il nome del cane: ")
        attr=input("inserisci la sua razza: ")
        anima=Animale(nome)
        cane=anima.creaCanide(attr)
        cane.stampa()
    elif(x=="3"):
        nome=input("inserisci il tipo di uccello: ")
        attr=input("inserisci il colore delle sue uova: ")
        anima=Animale(nome)
        volatile=anima.creaUccello(attr)
        volatile.stampa()  
    elif(x== "4"):
        break
    else:
        print("ATTENZIONE: devi inserire il numero corrispondente all'animale scelto")

