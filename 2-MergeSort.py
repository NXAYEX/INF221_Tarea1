def mergeSort(arreglo):
    """
    Esta función implementa el algoritmo MergeSort, que es un método de ordenamiento basado en la técnica de 
    divide y vencerás.Se divide el arreglo, lo ordena recursivamente y al final combina las partes ordenadas,
    dejando un orden de menor a mayor.

    Parámetros:
                arreglo(list): La lista de elementos a ordenar.
    Ejemplo de uso:
    >>> arreglo = [-2, 45, 0, 11, -9]
    >>> mergeSort(arreglo)
    >>> print(arreglo)
    [-9, -2, 0, 11, 45]
    """
    if len(arreglo)>1:
        #dividimos el arreglo
        r=len(arreglo)//2
        izq=arreglo[:r]
        der=arreglo[r:]
        #llamamos a la misma función pero con la parte dividida
        mergeSort(izq)
        mergeSort(der)
        i=j=k=0

        while i<len(izq) and j<len(der):
            if izq[i]<der[j]:
                arreglo[k]=izq[i]
                i+=1
            else:
                arreglo[k]=der[j]
                j+=1
            k+=1
        while i<len(izq):
            arreglo[k]=izq[i]
            i+=1
            k+=1
        while j<len(der):
            arreglo[k]=der[j]
            j+=1
            k+=1