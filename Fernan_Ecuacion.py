import math
     
a=int(input("Ingrese primer coeficiente: "))
b=int(input("Ingrese segundo coeficiente:"))
c=int(input("Ingrese tercer coeficiente: "))

disc=b*b-4*a*c
if(a!=0):
 if(disc<0):
  print("tiene raices imaginarias")
 else:
  x1=(-b+(math.sqrt(disc)))/(2*a)
  x2=(-b-(math.sqrt(disc)))/(2*a)
else:
    print("coefiente cuadratico debe ser diferente de cero")


def creartxt():
    archi=open ('Resultado de las raices.txt','w')
    archi.close()

def grabartxt():
    archi=open('Resultado de las raices.txt','a')
    archi.write("X1 = "+str(x1))
    archi.write("\tX2 = "+str(x2))
    archi.close()
    
def leertxt():
    archi=open('Resultado de las raices.txt','r')
    linea=archi.readline()
    while linea!="":
        print (linea)
        linea = archi.readline()
    archi.close



creartxt()
grabartxt()
leertxt()

  
