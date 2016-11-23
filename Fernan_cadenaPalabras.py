def leertxt():
    archi=open('Jeka.txt','r')
    linea=archi.readline()
    while linea!="":
        print (linea)
        linea = archi.readline()
    archi.close()

   
leertxt()


def contar():
    archi=open('Jeka.txt','r')
    archi1=open('resul.txt','w')
    nump=0
    for i in archi.readlines():
        palabras=i.split(" ")
        nump=nump+len(palabras)
    print("Numero de palabras que contiene el archivo: ", nump)
    archi1.write('Numero de palabras que contiene el archivo poema2.txt: '+str(nump))
    archi.close()
    archi1.close()


contar()
