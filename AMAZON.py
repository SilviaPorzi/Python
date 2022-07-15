class Amazon:
    Listafurgoni=[]
    def __init__(self):
        self.Listafurgoni
    #metodo che calcola il fatturato totale derivato dalla vendita degli oggetti di tutti i furgoni:
    def fatturato(self):
        sum=0
        for k in self.Listafurgoni:
            u=k*4
            sum=sum + u
        print("Il fatturato totale di lunedì, martedì e mercoledì è ", sum, "€")

class Furgone(Amazon):
    Listafurgone1=[]
    Listafurgone2=[]
    Listafurgone3=[]
    def __init__(self,nome):
        self.nomedelfurgone=nome
        Amazon.__init__(self)

#funzione che data una lista, e tre valori per lunedì, martedì e mercoledì, crea una lista con le quantità vendute in questi tre giorni
def inseriscifuori(Lista, l , mm ,me):
    Lista.append(l)
    Lista.append(mm)
    Lista.append(me)
    return Lista
#funzione che permette di aggiornare una lista aggiungendo nuovi valori per lunedì, martedì e mercoledì
def aggiornalista(Lista, l,m,n):
    try:
        Lista[0]=Lista[0]+int(l)
    except TypeError:
        print("inserisci un valore numerico")
    try:
        Lista[1]=Lista[1]+int(m)
    except TypeError:
        print("inserisci un valore numerico")
    try:    
        Lista[2]=Lista[2]+int(n)
    except TypeError:
        print("inserisci un valore numerico")
    return Lista

#ciclo che permette l'inserimento e l'aggiornamento delle quantità nei 3 tipi di furgone:
for i in range(3):
    while i==0:
        print("Aggiornamento furgone 001")
        g=input("Sei il furgone di Bartolini? Sì o no --> ")
        f1=Furgone("Bartolini")
        if g.lower() =="sì":
            inseriscifuori(f1.Listafurgone1, 3,6,7)
            print(f1.Listafurgone1)
            agg=input("Vuoi aggiornare le quantità vendute? sì o no -->")
            if agg.lower() =="sì":
                lu=input("Oggetti venduti lunedì: ")
                ma=input("oggetti venduti martedì: ")
                me=input("Oggetti venduti mercoledì: ")
                aggiornalista(f1.Listafurgone1,lu,ma,me)
                print(f1.Listafurgone1)
            elif agg.lower() == "no":
                break
            else:
                print("ATTENZIONE: puoi rispondere solo sì o no")
        elif(g.lower()=="no"):
            break
        else:
            print("ATTENZIONE: puoi rispondere solo sì o no")
    while i==1:
        print("Aggiornamento furgone 002:")
        g=input("Sei il furgone di FedEx? Sì o no --> ")
        f2=Furgone("FedEx")
        if g.lower() =="sì":
            inseriscifuori(f2.Listafurgone2, 8,9,1)
            print(f2.Listafurgone2)
            agg=input("Vuoi aggiornare le quantità vendute? sì o no -->")
            if agg.lower() =="sì":
                lu=input("Oggetti venduti lunedì: ")
                ma=input("oggetti venduti martedì: ")
                me=input("Oggetti venduti mercoledì: ")
                aggiornalista(f2.Listafurgone2,lu,ma,me)
                print(f2.Listafurgone2)
            elif agg.lower() == "no":
                break
            else:
                print("ATTENZIONE: puoi rispondere solo sì o no")
        elif(g.lower()=="no"):
            break
        else:
            print("ATTENZIONE: puoi rispondere solo sì o no")
    while i==2:
        print("Aggiornamento furgone 003:")
        g=input("Sei il furgone di Amazon? Sì o no --> ")
        f3=Furgone("Amazon")
        if g.lower() =="sì":
            inseriscifuori(f3.Listafurgone3, 8,9,1)
            print(f3.Listafurgone3)
            agg=input("Vuoi aggiornare le quantità vendute? sì o no -->")
            if agg.lower() =="sì":
                lu=input("Oggetti venduti lunedì: ")
                ma=input("oggetti venduti martedì: ")
                me=input("Oggetti venduti mercoledì: ")
                aggiornalista(f3.Listafurgone3,lu,ma,me)
                print(f3.Listafurgone3)
            elif agg.lower() == "no":
                break
            else:
                print("ATTENZIONE: puoi rispondere solo sì o no")
        elif(g.lower()=="no"):
            break
        else:
            print("ATTENZIONE: puoi rispondere solo sì o no")


Listafurgonicompleta=[f1.Listafurgone1, f2.Listafurgone2, f3.Listafurgone3]
print("La quantità dei prodotti venduti dei tre furgoni nei giorni di lunedì, martedì e mercoledì è: ", Listafurgonicompleta)

tuttiprodotti=Amazon()
#riempio la lista con i valori delle vendite di tutti i furgoni:
tuttiprodotti.Listafurgoni=f1.Listafurgone1+f2.Listafurgone2+f3.Listafurgone3
#calcolo e stampo il fatturato totale della vendita degli oggetti di tutti i furgoni
tuttiprodotti.fatturato()