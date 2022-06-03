import numpy as np
import random

def encriptado(texto):
    
    #ESCRIBA EN ESTA REGIÓN SU PROPUESTA DE SOLUCIÓN PARA EL ENCRIPTADO
    #USANDO EL MÉTODO EXPUESTO EN EL ENUNCIADO. ATÉNGASE AL USO DE LOS
    #RETORNOS PUESTOS AL FINAL DE ESTA FUNCIÓN

    len_texto= len(texto)
    
    clave = []
    newlst= []
    
    print(f" Tu texto a encriptar es: {texto}")
    #creacion de un diccionario con los valores de los cuadrados
    cuadrados = {}
    for i in range(1,50):
        n=1
        cuadrados[i]= i*i
        if len_texto in range(i*i):
            fila = i
            elm = i*i
            break
        n += 1
    print(cuadrados)
    cant_comodin = elm - len_texto
    n_texto = texto.ljust(len_texto + cant_comodin, "_" )
    print(n_texto)
    lista = list(n_texto)
    print(lista)
        
    #Se crea un diccionario para aleatorizacion de los indices
    d={}
    for x in range(0,elm):
        n=0
        d[x]= lista[x]
        n += 1
    #print(d)
    l = list(d.items())
    random.shuffle(l)
    d = dict(l)
    clave = list(d.keys())
    clave_valor= list(d.values())

    #funcion ord
 
    for caracter in clave_valor:
        newlst.append(ord(caracter))
 
    array_final = np.array(newlst).reshape(fila,fila)
   
    return array_final, clave


def desencriptado(array_encriptado, clave):
    
    #ESCRIBA EN ESTA REGIÓN SU PROPUESTA DE SOLUCIÓN PARA EL DESENCRIPTADO
    #USANDO EL MÉTODO EXPUESTO EN EL ENUNCIADO. ATÉNGASE AL USO DEL
    #RETORNO PUESTO AL FINAL DE ESTA FUNCIÓN
    
    texto =""
    lst = []
    caracter = []
    d= {}
    print("AQUI EMPIEZA LA DESENCRIPTACION--------")
    # Paso la matriz a una lista
    lst = array_encriptado.flatten().tolist()
    print("La lista del array:",lst)

    # Recorro la lista y convierto cada item en caracter
    for i in lst:
        caracter.append(chr(i))
    print("Texto desordenado:", caracter)
    #print("Mi clave es: " , clave)
    
    # Convierto las dos listas en diccionario, agragando por clave -valor

    for i in range(len(clave)):
      d[clave[i]] = caracter[i]
    
    # ordeno el diccionario
    
    orden = dict(sorted(d.items()))
    print(orden)

    valores = list(orden.values())
    # Elimino los "_" y armo el texto
    for letra in valores:
      if letra != "_":
        texto += letra

   
    return texto