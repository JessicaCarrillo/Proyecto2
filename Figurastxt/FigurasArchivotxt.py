print("                      ESCUELA POLITECNICA NACIONAL")
print("                  ESCUELA DE FORMACION DE TECNOLOGOS")
print("PROGRAMACION AVANZADA")
print("FERNANDA USHCASINA, JESICA CARRILLO")
print("PROYECTO")
print("FIRGURAS GEOMETRICAS")
import math
    
def aypTriangulo():
    print("Usted selecciono un *Triangulo* figura de 3 Lados")
    b = int(input("Ingresa base: "))
    h = int(input("Ingrese altura: "))
    area= b*h/2
    perimetro= 3*b
    print("el area es: " + str(area))
    print("el perimetro es: " + str(perimetro))
    ## GRABANDO RESULTADOS EN TXT
    archTri=open('TRIANGULO.txt','w')
    archTri=open('TRIANGULO.txt','a')
    archTri.write('Usted selecciono un *Triangulo* figura de 3 Lados \n')
    archTri.write('base ingresada:\t '+str(b))
    archTri.write('\taltura ingresada: '+str(h))
    archTri.write('\nEl area es: '+str(area))
    archTri.write('\nEl perimetro es : '+str(perimetro))
    archTri.close()

def aypCuadrado():
    print("Usted seleccinó un *Cuadrado* figura de 4 Lados")
    a = int(input("Ingrese lado: "))
    area = a * a
    perimetro = 4 * a
    print("el area es: " + str(area))
    print("el perimetro es: " + str(perimetro))
    ## GRABANDO RESULTADOS EN TXT
    archCuad=open('CUADRADO.txt','w')
    archCuad=open('CUADRADO.txt','a')
    archCuad.write('Usted seleccinó un un *Cuadrado* figura de 4 Lados \n')
    archCuad.write('lado ingresado:\t '+str(a))
    archCuad.write('\nEl area es: '+str(area))
    archCuad.write('\nEl perimetro es : '+str(perimetro))
    archCuad.close()
    
def aypPentagono():
    print("Usted selecciono un *Pentagono* figura de 5 Lados")
    lado = float(input("Ingrese Lado: "))
    radio= float(input("Ingrese radio: "))
    perimetro = lado*5 
    area = (perimetro*(radio**2-(lado/2)**2)**(1/2))/2 
    print("el area del pentagono es: " + str(area))
    print("el perimetro del pentagono es: " + str(perimetro))
    ## GRABANDO RESULTADOS EN TXT
    archPen=open('PENTAGONO.txt','w')
    archPen=open('PENTAGONO.txt','a')
    archPen.write('Usted selecciono un *Pentagono* figura de 5 Lados \n')
    archPen.write('lado ingresado:\t '+str(lado))
    archPen.write('\tradio ingresado: '+str(radio))
    archPen.write('\nEl area es: '+str(area))
    archPen.write('\nEl perimetro es : '+str(perimetro))
    archPen.close()
 
def aypHexagono():
    print("Usted selecciono un *Hexagono* figura de 6 Lados")
    lado = float(input("Ingrese Lado: "))
    radio= float(input("Ingrese radio: "))
    perimetro = lado*6 
    area = (perimetro*(radio**2-(lado/2)**2)**(1/2))/2 
    print ("El area es"+str(area) )
    print ("el perimetro es:"+ str(perimetro))
    ## GRABANDO RESULTADOS EN TXT
    archHexa=open('HEXAGONO.txt','w')
    archHexa=open('HEXAGONO.txt','a')
    archHexa.write('Usted selecciono un *Hexagono* figura de 6 Lados \n')
    archHexa.write('lado ingresado:\t '+str(lado))
    archHexa.write('\tradio ingresado: '+str(radio))
    archHexa.write('\nEl area es: '+str(area))
    archHexa.write('\nEl perimetro es : '+str(perimetro))
    archHexa.close()

def aypHeptagono():
    print("Usted selecciono un *Heptagono* figura de 7 Lados")
    lado = float(input("Ingrese Lado: "))
    radio= float(input("Ingrese radio: "))
    perimetro = lado*7 
    area = (perimetro*(radio**2-(lado/2)**2)**(1/2))/2 
    print ("El area es"+str (area ))
    print ("el perimetro es:"+str (perimetro))
    ## GRABANDO RESULTADOS EN TXT
    archHep=open('HEPTAGONO.txt','w')
    archHep=open('HEPTAGONO.txt','a')
    archHep.write('Usted selecciono un *Heptagono* figura de 7 Lados \n')
    archHep.write('lado ingresado:\t '+str(lado))
    archHep.write('\tradio ingresado: '+str(radio))
    archHep.write('\nEl area es: '+str(area))
    archHep.write('\nEl perimetro es : '+str(perimetro))
    archHep.close()
        
def aypOctagono():
    print("Usted selecciono un *Octagono* figura de 8 Lados")
    lado = float(input("Ingrese Lado: "))
    radio= float(input("Ingrese radio: "))
    perimetro = lado*8 
    area = (perimetro*(radio**2-(lado/2)**2)**(1/2))/2 
    print ("El area es"+ str (area ))
    print ("el perimetro es:"+str (perimetro))
    ## GRABANDO RESULTADOS EN TXT
    archOct=open('OCTAGONO.txt','w')
    archOct=open('OCTAGONO.txt','a')
    archOct.write('Usted selecciono un *Octagono* figura de 8 Lados \n')
    archOct.write('lado ingresado:\t '+str(lado))
    archOct.write('\tradio ingresado: '+str(radio))
    archOct.write('\nEl area es: '+str(area))
    archOct.write('\nEl perimetro es : '+str(perimetro))
    archOct.close()
        
  
def aypNonagono():
    print("Usted selecciono un *Nonagono* figura de 9 Lados")
    lado = float(input("Ingrese Lado: "))
    radio= float(input("Ingrese radio: "))
    perimetro = lado*9
    area = (perimetro*(radio**2-(lado/2)**2)**(1/2))/2 
    print ("El area es" +str (area ))
    print ("el perimetro es:"+str (perimetro))
    ## GRABANDO RESULTADOS EN TXT
    archNon=open('NONAGONO.txt','w')
    archNon=open('NONAGONO.txt','a')
    archNon.write('Usted selecciono un *Nonagono* figura de 9 Lados \n')
    archNon.write('lado ingresado:\t '+str(lado))
    archNon.write('\tradio ingresado: '+str(radio))
    archNon.write('\nEl area es: '+str(area))
    archNon.write('\nEl perimetro es : '+str(perimetro))
    archNon.close()

def aypDecagono():
    print("Usted selecciono un *Decagono* figura de 10 Lados")
    lado = float(input("Ingrese Lado: "))
    radio= float(input("Ingrese radio: "))
    perimetro = lado*10
    area = (perimetro*(radio**2-(lado/2)**2)**(1/2))/2 
    print ("El area es"+str( area ))
    print ("el perimetro es:"+str (perimetro))
    ## GRABANDO RESULTADOS EN TXT
    archDec=open('DECAGONO.txt','w')
    archDec=open('DECAGONO.txt','a')
    archDec.write('Usted selecciono un *Decagono* figura de 10 Lados \n')
    archDec.write('lado ingresado:\t '+str(lado))
    archDec.write('\tradio ingresado: '+str(radio))
    archDec.write('\nEl area es: '+str(area))
    archDec.write('\nEl perimetro es : '+str(perimetro))
    archDec.close()
    
def Intentar():
    while(again!="no"):
        menu()
    
def menu():
    print("LISTA DE FIGURAS QUE CONTIENE EL PROGRAMA")
    print("Area y perimetro de una figura geometrica regular")
    print("3. Triangulo")
    print("4. Cuadrado")
    print("5. Pentagono")
    print("6. Hexagono")
    print("7. Heptagono")
    print("8. Octagono")
    print("9. Nonagono")
    print("10. Decagono")
    global opcion
    opcion=int(input("Ingrese el numero de lados de la figura: "))
    if(opcion==1):
        print("No existe una figura de un solo lado")
        print("Ingrese numero de lados correctos \n")
        opcion
    elif(opcion==2):
        print("No existe una figura de dos lados")
        print("Ingrese numero de lados correctos \n")
        opcion
    elif(opcion==3):
        aypTriangulo()
    elif(opcion==4):
        aypCuadrado()
    elif(opcion==5):
        aypPentagono()
    elif(opcion==6):
        aypHexagono()
    elif(opcion==7):
        aypHeptagono()
    elif(opcion==8):
        aypOctagono()
    elif(opcion==9):
        aypNonagono()
    elif(opcion==10):
        aypDecagono()
    else:
        print("Opcion ingresada incorrecta")
    print("Quieres elegir nuevamente(si/no)")
    global again
    again=input()
    again=again.lower()
    Intentar()



menu()
