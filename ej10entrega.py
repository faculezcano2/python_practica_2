'''
10. Dada una lista de nombres de estudiantes y dos listas con sus notas en un curso, escriba un programa que manipule dichas estructuras de datos para poder resolver los siguientes puntos:
    1. Generar una estructura con todas las notas relacionando el nombre del estudiante con las notas. Utilizar esta estructura para la resolución de los siguientes items.
    2. Calcular el promedio de notas de cada estudiante.
    3. Calcular el promedio general del curso.
    4. Identificar al estudiante con la nota promedio más alta.
    5. Identificar al estudiante con la nota más baja.


**Nota**:
- Las 3 estructuras están ordenadas de forma que los elementos en la misma posición corresponden a un mismo alumno.
- Realizar funciones con cada item


# Entrega 2
### Pautas
   * Suba la resolución total del **ejercicio 10** al repositorio individual de Github, luego elija uno de los siguientes items: A,C,D o E y realice un video explicando cómo lo resolvió y las decisiones que tomó implementando map, zip, lambda (por qué utilizó cada estructura de datos o estructura de control) y muestre la ejecución del programa en la terminal.
   * **Duración máxima del video**: 5 minutos

   * **Puntos**: 15.
   * **Fecha límite de entrega**: Viernes, 14 de abril de 2023, 23:59
   * **Modalidad de entrega**: Subir el programa al repositorio de github y copie el enlace del repositorio  junto con el link del video en la resolución de la tarea de Cátedras.



'''



nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 'David',
'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 'Francsica', 
'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 'Joaquina', 'Jorge',
'JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana','LAUTARO', 'Leonel', 'Luisa', 
'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 'Nicolás',  'Nancy', 'Noelia', 'Pablo', 
'Priscila', 'Sabrina', 'Tomás', 'Ulises', 'Yanina' '''
notas_1 = [81,  60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 12, 77, 
           13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 85, 73, 37, 42, 95, 18, 7, 
           74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37, 64, 13, 8,
           87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73, 95, 19, 47, 15, 31,
           39, 15, 74, 33, 57, 10]


def notas_con_estudiantes(listaN,lista1,lista2):
    '''
    lo que hace esta funcion es poner una lista de nombres y dos listas de notas en una sila lista
    '''
    listaN = listaN.split(",")
    notas = list(zip(listaN,lista1,lista2))
    return notas

nombres_en_lista= nombres.split(",")



def promedio(notas):
    '''
    lo que hace esta funcion es recibir una lista de tuplas en la cual hay un nombre y dos notas y ponerle el promedio de esas dos notas al nombre
    '''
    lista_notas = list(notas)
    prom = lambda lista_notas: ((lista_notas[1]+lista_notas[2])/2)
    promedios = map(prom,notas)
    terminado = list(zip(nombres_en_lista,promedios))
    return terminado

def prom_general(notas):
    '''
    lo que hace esta funcion es recibir una lista de promedios y dar el promedio general
    '''
    l1 = sum(x[1] for x in notas)
    resultado = (l1/len(notas))
    return(resultado)

def estudiante_prom_mas_alto(lista):
    '''' 
    lo que hace esta funcion es recibir una lista de estudiantes y sus promedios y devolver el prom mas alto
    '''
    max_valor = max(lista, key=lambda x:x[1])#saco el mayor por el segundo elem de la tupla
    return max_valor

def estudiante_nota_mas_bajo(notas):
    ''' 
    lo que hace esta funcion es recibir una lista de tuplas donde esta hay un nombre y dos notas y devolver el estudiante con la nota mas baja
    '''
    lista_notas = list(notas)
    suma_notas = lambda lista_notas: ((lista_notas[1]+lista_notas[2]))
    sumas = map(suma_notas,notas)
    terminado = list(zip(nombres_en_lista,sumas))
    minimo = min(terminado, key = lambda x:x[1])
    print(minimo)





notas_con_nombre = notas_con_estudiantes(nombres,notas_1,notas_2)#inciso1
print(notas_con_nombre)
promedios = promedio(notas_con_nombre)#inciso2
print(promedios)
prome_general = prom_general(promedios)
print(prome_general)
estudiante_prom_mas_alto(notas_con_nombre)
estudiante_nota_mas_bajo(notas_con_nombre)
