
def QuickSort(arreglo,star,end):
    """
    Esta función implementa el algoritmo Quicksort, que es un método de ordenamiento
    eficiente basado en la técnica de divide y vencerás. La función selecciona un 
    pivote y particiona el arreglo: menores al pivote y mayores al pivote. Luego, 
    aplica recursivamente el mismo proceso a los subarreglos.
    
    Parámetros:
            arreglo(list): La lista de elementos a ordenar.
            star(int): El índice inicial del segmento del arreglo a ordenar.
            end(int): El índice final del segmento del arreglo a ordenar.
    Ejemplo de uso:
    >>> arreglo = [-2, 45, 0, 11, -9]
    >>> QuickSort(arreglo, 0, len(arreglo) - 1)
    >>> print(arreglo)
    [-9, -2, 0, 11, 45]
    """
    if star<end:
        #el pivote va a ser el primer elemento de la lista.
        pivote=arreglo[star]
        i=star+1
        j=end
        while True:
            while i<=j and arreglo[i]<=pivote:
                i+=1
            while i<=j and arreglo[j]>=pivote:
                j-=1
            if i<=j:
                arreglo[i],arreglo[j]=arreglo[j],arreglo[i]
            else: break
        arreglo[star],arreglo[j]=arreglo[j],arreglo[star]

        #hacemos llamada recursiva al lado izq
        QuickSort(arreglo,star,j-1)
        #al lado der
        QuickSort(arreglo,j+1,end)
# Ejemplo de uso
arreglo= [-2, 45, 0, 11, -9]
QuickSort(arreglo, 0, len(arreglo) - 1)
print("Arreglo ordenado:", arreglo)
print("####")
################### FUNCION DE SORTING DE PYTHON ##############
arreglo.sort()
print(arreglo)