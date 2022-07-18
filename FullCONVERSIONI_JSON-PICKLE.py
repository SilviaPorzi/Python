import json
import pickle
import pprint

dizio = {"a" :11, "b" :24, "c" :11} 
frase = "Siamo la classe migliore di "

def modificaC(dizio,x):
    dizio=dizio.update({"c":x})
    return dizio

print("Scegli come vuoi inserire l'oggetto dizionario in \n 1. Json \n 2. Pickle ")
ris1=input("> ")
while True:
    if(ris1=="1"):
        x=json.dumps(dizio)
        y=json.loads(x)
        print(y)
        num=input("Scegli un valore da sostituire alla chaive c: ")
        modificaC(y,num)
        print(y)
        ris2=input("Vuoi tornare in file Pickle? ")
        if(ris2=="si"):
            modificoy=pickle.dumps(y)
            z=pickle.loads(modificoy)
            pprint.pprint(z)
            break
        elif(ris2=="no"):
            print("Il file importato è rimasto Json")
            break
        else:
            print("ATTENZIONE: puoi rispondere solo si o no")
            continue            
    elif(ris1=="2"):
        x=pickle.dumps(dizio)
        y=pickle.loads(x)
        print(y)
        num=input("Scegli un valore da sostituire alla chaive c: ")
        modificaC(y,num)
        pprint.pprint(y)
        ris2=input("Vuoi tornare in file Json? ")
        if(ris2=="si"):
            modificoy=json.dumps(y)
            z=json.loads(modificoy)
            print(z)
            break
        elif(ris2=="no"):
            print("Il file importato è rimasto Pickle") 
            break
        else:
            print("ATTENZIONE: puoi rispondere solo si o no")
            continue
    else:
        print("ATTENZIONE: puoi rispondere solo si o no")
        continue

print("Scegli come vuoi inserire la frase 'Siamo la classe migliore di' \n 1. Json \n 2. Pickle ")
ris3=input("> ")
while True:
    if(ris3=="1"):
        x=json.dumps(frase)
        y=json.loads(x)
        y=y+input("inserisci termine di paragone: ")
        print(y)
        ris4=input("Vuoi tornare in file Pickle? ")
        if(ris4=="si"):
            ymodifico=pickle.dumps(y)
            z=pickle.loads(ymodifico)
            pprint.pprint(z)
            break
        elif(ris4=="no"):
            print("Il file importato è rimasto Pickle") 
            break
        else:
            print("ATTENZIONE: puoi rispondere solo si o no")
            continue
    elif(ris3=="2"):
        x=pickle.dumps(frase)
        y=pickle.loads(x)
        y=y+input("inserisci termine di paragone: ")
        pprint.pprint(y)
        ris4=input("Vuoi tornare in file Json? ")
        if(ris4=="si"):
            ymodifico=json.dumps(y)
            z=json.loads(ymodifico)
            print(z)
            break
        elif(ris4=="no"):
            print("Il file importato è rimasto Pickle") 
            break
        else:
            print("ATTENZIONE: puoi rispondere solo si o no")
            continue
    else:
        print("ATTENZIONE: puoi rispondere solo si o no")
        continue

