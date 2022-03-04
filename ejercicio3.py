#Manejo de listas

"""
*************************************
            Manejo de Listas
*************************************
"""
def listas():
    lista1= []
    lista2 = list()

    listaConElementos=[30, 2000000,"Geraldine Suarez", "Ingeniera", True, ["Tecnico", "Profesional", "doctorado", 4]] #Los elementos estan separados por comas (,)
    #print(listaConElementos[1]) #imprime el elemento de la posicion 1 que es 2000000

#utilizando el ciclo for
    #for i in range(6): #va desde 0 hasta 6
    for i in range(len(listaConElementos)):
        print(listaConElementos[i])
#utilizando el ciclo while
    print("")
    print("ciclo While")
    j=0
    while j < len(listaConElementos):
        print(listaConElementos[j])
        j=j+1 #es lo mismo que j+=1

    listaConElementos[1] = listaConElementos[1] +200000


    print("")
    print(listaConElementos[-1][3]) #Del ultimo elemento muestreme la posicion 3
    print(listaConElementos[5][3]) #muestra la posicion 3
    print(listaConElementos[0:3]) #Muestra desde la posicion 0 a 2, no incluye la 3
    print(listaConElementos[0:6:2]) #posicion inicial: posicion final: avanza de 2 en 2

    #listaConElementos.append(["Sede Riohacha", "Miguel"]) #Agrega elementos al final de la lista
    listaConElementos.insert(2, ["Sede Riohacha", "Miguel"]) #Agrega un elemento en la posición que yo desee
    print(listaConElementos)

    del listaConElementos[2] #Remover elemento de la posicion indicada
    print(listaConElementos)

    listaConElementos.remove("Ingeniera") #Borra por el contenido 
    print(listaConElementos)











def main (): 
    listas()

if __name__ == "__main__":
    main()