import random
########Listas#####
def listas_aleatorias(tamano,minimo,maximo):
    return[random.randint(minimo,maximo) for i in range(tamano)]

#print(listas_aleatorias(6,0,3))
def listas_semiOrdenada(tamano):
    lista=list(range(tamano))
    ordenado=0.7
    num_desordenado=int(tamano*(1-ordenado))
    indices=random.sample(range(tamano),num_desordenado)
    for i in indices:
        lista[i]=random.randint(0,tamano)
    return lista
print(listas_semiOrdenada(6))

######## Matriz cuadrada n*n ##########
def matriz_cuadrada(n,minimo,maximo):
    """
    Función para generar matriz cuadrada con elementos aleatorios.
    Parámetros:
            n(int): Es el tamaño de nuestra matriz cuadrada.
            minimo(int):El valor minimo que puede tener los números aleatorios.
            maximo(int):El valor maximo que puede tener los números aleatorios.
    """
    return[[random.randint(minimo,maximo) for i in range(n)] for j in range(n)]
#matriz=matriz_cuadrada(9,0,3)
#print(matriz)
######### matriz no cuadrada n*m ###########
def matriz_no_cuadrada(n,m,minimo,maximo):
    return[[random.randint(minimo,maximo) for i in range(m)] for j in range(n)]
########## GUARDAR EN ARCHIVO TXT #################
def listas_en_txt(lista,archivo_nombre="Dataset_Listas.txt"):
    with open(archivo_nombre, 'a') as archivo:
        archivo.write(' '.join(map(str, lista)) + '\n')

def matrices_en_txt(matriz,archivo_nombre="Dataset_matrices.txt"):
    with open(archivo_nombre, 'a') as archivo:
        for fila in matriz:
            archivo.write(' '.join(map(str, fila))+'\n')
#Cramos listas no ordenadas y ordenadas
l1=listas_aleatorias(1000,0,10)
l2=listas_aleatorias(100,0,10)
l3=listas_semiOrdenada(1000)
l4=listas_semiOrdenada(100)
#Creamos matriz cuadrada y no cuadrada
A =matriz_cuadrada(10,0,10)
B =matriz_cuadrada(10,0,10)

C =matriz_no_cuadrada(5,4,0,10)
#Guardar en el txt
listas_en_txt(l1)
listas_en_txt(l2)
listas_en_txt(l3)
listas_en_txt(l4)
matrices_en_txt(A)
matrices_en_txt(B)
matrices_en_txt(C)

