#5.	Una tienda de juguetes tiene mucho éxito con dos de sus productos: payasos y muñecas. 
#Realiza ventas por correo y la empresa de logística les cobra por el peso de cada paquete, 
#por lo que deben calcular el peso total de los payasos y muñecas que se enviarán en cada 
#paquete según la demanda. Cada payaso pesa 112 g y cada muñeca pesa 75 g. Escribir un programa 
#que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total 
#del paquete que será enviado.
pesopayaso=112
pesomuñeca=75
cantpayaso=0
cantmuñeca=0
pesototalpayaso=0
pesototalmuñeca=0
total=0
print("Ingrese la cantidad de payasos de este pedido")
cantpayaso=float(input())
print("Ingrese la cantidad de muñecas de este pedido")
cantmuñeca=float(input())
pesototalpayaso=cantpayaso*pesopayaso
pesototalmuñeca=cantmuñeca*pesomuñeca
total=pesototalmuñeca+pesototalpayaso
print("El peso total en payasos es de: ", pesototalpayaso, "g")
print("El peso total en muñecas es de: ", pesototalmuñeca, "g")
print("El peso total del pedido es: ", total, "g")