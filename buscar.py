#Creamos la lista b
lista = [
    [3,5,7],
    [5,8,7],
    [1,6,10]
    ]

#Declaramos la funcion buscar con párametros l,n
def buscar(l,n):

    for i  in range(len(lista)):  #Iterador i recorre la fila
        for j in range(len(lista[i])) : #Iterador j recorre las columnas
          if lista[i][j]  == n :  #Comparamos si la posicion en i y j  es igual al numero que deseamos buscar

              return i,j # retornamos ambos iteradores

    return "No se encontro el numero" # si no encuentra el numero que estamos buscando en la lista retorna un mensaje

for i in lista:  #Imrprimimos la lista
  print(i)

print("El numero esta en la posición ",buscar(lista,10))
