

print("\nLISTA")

#ORDENAR LISTA
def orden(f):

    n = len(f) # Declaramos la variable que cuente la fila
    for i in range(n):
        for k in range(0, n-i-1):
            if f[k] > f[k+1]:  #Comparamos si la posicion es mayor a la posicion mas uno
                f[k], f[k+1] = f[k+1], f[k]  # Si es mayor la posicion que la posicion de j + 1 cambiamos los valores

list = [
    [8,7,6],
    [15,12,6],
    [7,3,2]
    ]


# Imprimimos la lista con nuestros elementos
for fil in list :
  print(fil)


num = int(input("Ingrese la fila que quiere ordenar: ")) #Declaramos una variable para decir que fila ordenamos
orden(list[num])  #Definimos la función y llenamos el parametro
# Imprimimos  la lista  después de ordenar, y seleccionamos la fila
print(f"\nLa lista ordenada de la fila {num} es")
for file in list:
    print(file)
