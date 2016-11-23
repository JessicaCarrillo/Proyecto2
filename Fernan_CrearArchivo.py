def creartxt():
    archi=open ('datos.txt','w')
    archi.close()

def grabartxt():
    archi=open('datos.txt','a')
    archi.write('Fernanada\n')
    archi.write('Jessica\n')
    archi.close()


creartxt()
grabartxt()
