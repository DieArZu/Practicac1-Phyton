#2.	Crear un programa que solicite al usuario su peso (en kg) y estatura (en metros), 
#calcule el índice de masa corporal y lo guarde en una variable. Finalmente, 
#mostrar en pantalla la frase "Tu índice de masa corporal es <imc>" donde <imc> es el 
#índice de masa corporal calculado redondeado con dos decimales.
peso=0.00
altura=0.00
print("Ingrese la altura en metros")
altura=float(input())
print("Ingrese peso en kilogramos")
peso=float(input())
imc=peso/(altura*altura)
imcc=round(imc,2)
print("Tu el índice de masa corporal es: ",imcc)