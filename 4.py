#4.	Crear un programa que pregunte al usuario una cantidad para invertir, 
#la tasa de interés anual y el número de años, y muestre en pantalla el 
#capital obtenido en la inversión.
capital=0.00
interes=0.00
años=0.0
moninter=0.0
montotal=0
print("Ingrese el monto a invertir")
capital=float(input())
print("Ingrese el porcentra de interes anual %")
interes=float(input())
print("Ingrese la cantidad de años de la inversion")
años=float(input())
moninter=capital*años*(interes/100)
montotal=capital+moninter
montinter=round(moninter,2)
monttotal=round(montotal,2)
print("El monto ganado por inetereses es de:",montinter)
print("El monto total a recibir al término del periodo (capital+interes) es de  ", monttotal)
