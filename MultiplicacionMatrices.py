import random
import numpy as np
#################### ALGORITMO ITERATIVO CÚBICO TRADICIONAL ###########
def tradicional(A,B):
    """Multiplica matrices de manera tradicional.
    Parámetros:
            A(list of list of int): Primera matriz.
            B(list of list of int): segunda matriz.
    Notas:
        - La matriz A debe tener tantas columnas como filas tiene la matriz B.
        - La matriz resultado C tendrá el mismo número de filas que A y el mismo número de columnas que B.
    """
    #matriz resultado con mismas filas que A y tantas columnas como B
    C=[[0]*len(A) for _ in range(len(A))]
    #recorrer cada fila de A y cada columna de B
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j]+=A[i][k]*B[k][j]
    return C
############ ALGORITMO ITERATIVO CUBICO OPTIMIZADO #####################
def Optimizado(A,B):
    """Multiplica matrices de manera trasponiendo la segunda matriz B.
    Parámetros:
            A(list of list of int): Primera matriz.
            B(list of list of int): segunda matriz.
    """
    t=[]
    #trasponiendo la segunda matriz
    for i in range(len(B[0])):
        t.append([])
        for j in range(len(B)):
            t[i].append(B[j][i])
    print(t)
    #multiplicar con la matriz normal
    C=[[0]*len(A) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(t[0])):
            for k in range(len(t)):
                C[i][j]+=A[i][k]*t[k][j]
    return C
########### ALGORITMO STRASSEN #########################################
def strassen(A,B):
    A = np.array(A)
    B = np.array(B)
    #solo funciona para funciones cuadradas
    n=len(A)
    if n==1:
        return A*B
    else:
        #dividir matrices
        a11=A[:n//2,:n//2]
        a12=A[:n//2,n//2:]
        a21=A[n//2:,:n//2]
        a22=A[n//2:,n//2:]

        b11=B[:n//2,:n//2]
        b12=B[:n//2,n//2:]
        b21=B[n//2:,:n//2]
        b22=B[n//2:,n//2:]
        #print(a11,a22)
        m1=strassen(a11+a22,b11+b22)
        m2=strassen(a21+a22,b11)
        m3=strassen(a11,b12-b22)
        m4=strassen(a22,b21-b11)
        m5=strassen(a11+a12,b22)
        m6=strassen(a21-a11,b11+b12)
        m7=strassen(a12-a22,b21+b22)
        #valores finales de c
        c11=m1+m4-m5+m7
        c12=m3+m5
        c21=m2+m4
        c22=m1-m2+m3+m6
        #ensambar
        C=np.zeros((n,n))
        C[:n//2,:n//2]=c11
        C[:n//2,n//2:]=c12
        C[n//2:,:n//2]=c21
        C[n//2:,n//2:]=c22
        return C
