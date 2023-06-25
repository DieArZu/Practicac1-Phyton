#6.	Imagina que recién abres una nueva cuenta de ahorros que te ofrece una tasa de interés del 4% anual.
# Los intereses de estos ahorros, que no se cobran hasta finales de año, se agregan al saldo final de tu 
#cuenta de ahorros. Escribir un programa que lea la cantidad de dinero depositada en la cuenta de ahorros,
#introducida por el usuario. Luego, el programa debe calcular y mostrar en pantalla la cantidad de ahorros 
#después del primer, segundo y tercer año. Redondear cada cantidad a dos decimales.
montoahorro0=0
print("Digite la cantidad por ahorrar")
montoahorro0=float(input())
totaño1=montoahorro0*0.04+montoahorro0
totaño2=totaño1*0.04+totaño1
totaño3=totaño2*0.04+totaño2
totaño3r=round(totaño3,2)
print("La cantidad de ahorros al final del 1er año es: ",totaño1)
print("La cantidad de ahorros al final del 2do año es: ",totaño2)
print("La cantidad de ahorros al final del 3er año es: ",totaño3r)
