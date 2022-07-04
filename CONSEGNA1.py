class primaclasse():

 x = 1  #integer
 y="mirko" #stringa
 m=1,65 #float(massimo 7 caratteri)
 b=True
 e=""
 e=False
 e=0 #modalità implicita di falsità in Python

nome=input("come ti chiami?")
if(nome != False):
    età=input("quanti anni hai?")
    if(età != False):
        print(nome + " ha " + età + " anni")
else:
  print("inserire nome ed età")

Dati=[nome,età]
if(Dati != False):
    if(nome != False):
        if(età!= False):
         print(Dati)
        else:
         print("Inserire l'età")
    else:
     print("Inserire il nome")
else:
    print("Lista incompleta")

if(nome!="Silvia"):
    Dati.remove(nome)
    if(età!="35"):
        Dati.remove(età)
        print(Dati)    
    print("I dati inseriti non sono dello studente Silvia")
else:
    print("I dati inseriti sono dello studente Silvia")