#7.	Una panadería vende barras de pan a 3000 cada una. El pan que no es fresco tiene un descuento del 60%. 
#Escribir un programa que comience leyendo el número de barras vendidas que no son frescas. Luego,
#el programa debe mostrar el precio regular de una barra de pan, el descuento aplicado por no ser fresca 
#y el costo total final.
cantpan=0
desc=0
total=0
print("Ingrese la cantidad de barras de pan no fresco")
cantpan=float(input())
precioregular=3000*cantpan
desc=precioregular*0.6
total=precioregular-desc
print("El precio regular de ",cantpan," barras de pan es de:",precioregular)
print("El descuento en las ",cantpan," barras de pan no fresco es ",desc)
print("El precio total con el descuento no fresco es de: ",total)