#3.	Crear un programa que solicite al usuario dos números enteros y muestre en pantalla la <n> 
#dividido entre <m> da un cociente <c> y un residuo <r>, donde <n> y <m> son los números ingresados 
#por el usuario, y <c> y <r> son el cociente y residuo de la división entera, respectivamente.
n=0.00
m=0.00
c=0.0
r=0.0
print("Ingrese el valor del dividendo")
n=float(input())
print("Ingrese el valor del divisor")
m=float(input())
c=n/m
r=n%m
coci=round(c,2)
recid=round(r,2)
print("La division de ",n," entre ",m," da un cociente de ",coci," y un reciduo de ",recid)
