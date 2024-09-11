def SelectionSort(arreglo):
    """
    Esta función implementa el algoritmo Selection Sortq que ordena un arreglo encontrando repetidamente 
    el elemento más pequeño de la parte no ordenada y colocándolo al 
    principio.

    Parámetros:
            arreglo(list): La lista de elementos a ordenar.
    Ejemplo de uso:
    >>> arreglo = [-2, 45, 0, 11, -9]
    >>> SelectionSort(arreglo)
    >>> print(arreglo)
    [-9, -2, 0, 11, 45]
    """
    tamano=len(arreglo)
    for step in range(tamano):
        minimo=step
        for i in range(step+1,tamano):
            if arreglo[i]<arreglo[minimo]:
                minimo=i
        #tenemos que intercambiar el elemento minimo con el primero
        arreglo[step],arreglo[minimo]=arreglo[minimo],arreglo[step]
        
data = [-2, 45, 0, 11, -9]
SelectionSort(data)
print('Complejidad Ordenación: O(n^2)')
print(data)