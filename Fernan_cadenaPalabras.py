def leertxt():
    archi=open('poema2.txt','r')
    linea=archi.readline()
    while linea!="":
        print (linea)
        linea = archi.readline()
    archi.close()

   
leertxt()


