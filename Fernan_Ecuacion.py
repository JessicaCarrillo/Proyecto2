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
  
