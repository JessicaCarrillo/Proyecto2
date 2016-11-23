def creartxt():
    archi=open ('datos.txt','w')
    archi.close()

def grabartxt():
    archi=open('datos.txt','a')
    archi.write('Programacion Avanzada\n')
    archi.write('Aula 16\n')
    archi.write('Fernanada\t')
    archi.write('Ushcasina\nt')
    archi.write('Jessica \t')
    archi.write('Carrillo\t')
    archi.close()
    
def leertxt():
    archi=open('datos.txt','r')
    linea=archi.readline()
    while linea!="":
        print (linea)
        linea = archi.readline()
    archi.close


creartxt()
grabartxt()
leertxt()

