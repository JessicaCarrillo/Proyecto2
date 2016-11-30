def leerH():
    archi=open('HarryPotter.txt','r')
    linea=archi.readline()
    while linea!="":
        print(linea)
        linea=archi.readline()
    archi.close

leerH()

def contarH():
    archi=open('HarryPotter.txt','r')
    archiH=open('ResultadoContar.txt','w')
    p=0
    for i in archi.readlines():
        palabras=i.split(" ")
        p=p+len(palabras)
    print("\nel total de palabras es: ",p)
    archiH.write("el total de palabras es: "+str(p))
    archi.close()
    archiH.close()

contarH()

def palabH():
    palabra=input("ingrese palabra a  buscar: ")
    archiH=open('ResultadoContar.txt','a')
    archi=open('HarryPotter.txt','r')
    
    repeti=0
    lineas=archi.readlines()
    for line in lineas:
        palabras=line.split(" ")
        for p in palabras:
            if p==palabra:
                repeti=repeti+1
    print("la palabra: ",palabra,"\nse repite: ",repeti)
    print("(",palabra,",",repeti,")")
    archiH.write("\n("+str(palabra))
    archiH.write(","+str(repeti)+")")
    archi.close
    archiH.close
    
    
def denuevoH():
    global nuevo
    print("Desea intentar nuevamente(si/no)")
    nuevo=input()
    nuevo=nuevo.lower()
    while(nuevo!="no"):
        palabH()
        denuevoH()

palabH()
denuevoH()

    




