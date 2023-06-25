# Crear un programa que consulte al usuario por la cantidad de horas trabajadas y el costo por hora.
# Luego debe mostrar en pantalla el salario que le corresponde.
horas=0
costo=0
print("Ingrese la cantidad de horas trabajadas")
horas=int(input())
print("Ingrese el valor de las horas")
costo=int(input())
resul = horas*costo
print("El salario correspondiente es de: ",resul)