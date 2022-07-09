class Esserevivente():
    Listadettagliata=[]
    def __init__(self,R,N):
        self.regno=R
        self.nome=N
    def attributiLISTA(self):
        self.Listadettagliata.append(self.regno)
        self.Listadettagliata.append(self.nome)
    def printattributi(self):
        print(self.regno, self.nome)

class RegnoAnimale(Esserevivente):
    
    ListaAnimale=[]

    def __init__(self, R, N, S):
        Esserevivente.__init__(self, R, N)
        self.specieanimale=S
        self.attributiLISTA()

    def attributiLISTA(self):
        self.ListaAnimale.append(self.regno)
        self.ListaAnimale.append(self.nome)
        self.ListaAnimale.append(self.specieanimale)
    

    def listareattributi(self):
        list(self.attributiLISTA)

    def printattributi(self):
        print(self.regno, self.nome, self.specieanimale)

class RegnoVegetale(Esserevivente):
    ListaVegetale=[]
    def __init__(self, R, N, T):
        Esserevivente.__init__(self, R,N)
        self.tipovegetale=T
        self.attributiLISTA()

    def attributiLISTA(self):
        self.ListaVegetale.append(self.regno)
        self.ListaVegetale.append(self.nome)
        self.ListaVegetale.append(self.tipovegetale)

    def printattributi(self):
        print(self.regno, self.nome, self.tipovegetale)


LISTA_TOTALE=[]

while True:
    
    

    print("--TIPO DI ESSERE VIVENTE-- \n 1. ANIMALE \n 2. VEGETALE \n 3. NESSUNO DEI PRECEDENTI")
    x=input("> ")
    if(x=="ANIMALE"):
        nomeAn=input("Come ti chiami? ")
        specieAn=input("Di che specie sei? ")
        tipo_An=RegnoAnimale("Fauna", nomeAn, specieAn)
        #tipo_An.printattributi()
        #tipo_An.attributiLISTA()
        LISTA_TOTALE.append(RegnoAnimale.ListaAnimale)
        
    elif(x=="VEGETALE"):
        nomeVeg=input("Come ti chiami? ")
        chetipo=input("Che tipo di essere vegetale sei? ")
        tipo_Veg=RegnoVegetale("Flora", nomeVeg, chetipo)
        #tipo_Veg.printattributi()
        LISTA_TOTALE.append(RegnoVegetale.ListaVegetale)
        
    elif(x=="NESSUNO DEI PRECEDENTI"):
        print("Lista degli esseri viventi intervistati: ", LISTA_TOTALE)
        break    
        
    else:
        print("Non ho capito la tua risposta, digita in maniera corretta una delle tre opzioni elencate")

contoAnimali=int(len(RegnoAnimale.ListaAnimale)/3)   
contoVegetali=int(len(RegnoVegetale.ListaVegetale)/3)  
print("Animali: ",contoAnimali, RegnoAnimale.ListaAnimale)
print("Vegetali: ",contoVegetali, RegnoVegetale.ListaVegetale)