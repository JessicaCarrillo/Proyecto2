def leertxt():
    archi=open('Poema.txt','r')
    linea=archi.readline()
    while linea!="":
        print (linea)
        linea = archi.readline()
    archi.close
    
leertxt()

